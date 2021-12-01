import os
from django.conf import settings
from datetime import date
from decimal import Decimal as D
from django.db.models import F, Func, Value, CharField
from django.db.models import Avg, Max, Min, Value, ExpressionWrapper
from django.db.models.functions import Coalesce
from django.db.models import DecimalField
from .models import BanxicoModel
from .utils import convert_date_to_str, convert_str_to_date
import requests
import json


class BaxincoService:

    def __init__(self):
        self.token = settings.TOKEN
        self.base_url = "https://www.banxico.org.mx/SieAPIRest/service/v1/series/SP68257,SF43718/datos"
        self.udis_id = "SP68257"
        self.dolar_id = "SF43718"

    def get_url(self, date_start, date_end):
        return self.base_url + '/{0}/{1}'.format(date_start, date_end)

    def get_model_data(self, date_start, date_end):
        queryset = BanxicoModel.objects.filter(
            date__gte=date_start, date__lte=date_end).annotate(
                str_date=ExpressionWrapper(Func(
                    F('date'),
                    Value('%d-%m-%Y'),
                    function='DATE_FORMAT'),
                    output_field=CharField()
                )
        ).order_by('date')
        data = {
            'queryset': queryset,
            'date': list(queryset.values_list('str_date', flat=True)),
            'dolar': {
                'values': list(queryset.values_list('dolar', flat=True)),
                'max': queryset.aggregate(max=Coalesce(Max('dolar'), Value(D(0))))['max'],
                'min': queryset.aggregate(min=Coalesce(Min('dolar'), Value(D(0))))['min'],
                'avg': queryset.aggregate(avg=Coalesce(Avg('dolar'), Value(D(0))))['avg'],
            },
            'udis': {
                'values': list(queryset.values_list('udis', flat=True)),
                'max': queryset.aggregate(max=Coalesce(Max('udis'), Value(D(0))))['max'],
                'min': queryset.aggregate(min=Coalesce(Min('udis'), Value(D(0))))['min'],
                'avg': queryset.aggregate(avg=Coalesce(Avg('udis'), Value(D(0))))['avg'],
            }
        }
        return data

    def validate_queryset(date_start, date_end):
        queryset = BanxicoModel.objects.filter(date__gte=date_start,
                                               date__lte=date_end).order_by('-date')
        return queryset

    def parse_data(self, data):
        bmx = data.get('bmx')
        series = bmx.get('series')
        data = {}
        for serie in series:
            id_serie = serie.get('idSerie')

            if id_serie == self.dolar_id:
                attr = 'dolar'
            else:
                attr = 'udis'
            for dato in serie.get('datos'):
                date = dato.get('fecha')
                if data.get(date):
                    data[date][attr] = dato.get('dato')
                else:
                    data[date] = {attr: dato.get('dato')}
        return self.parse_data_with_model(data)

    def parse_data_with_model(self, data):
        new_data = []
        for key, value in data.items():
            model = BanxicoModel(date=convert_str_to_date(
                key), dolar=D(value.get('dolar', 0)), udis=D(value.get('udis', 0)))
            new_data.append(model)
        return new_data

    def create_or_update_model(self, data):
        data = self.parse_data(data)
        BanxicoModel.objects.bulk_update_or_create(
            data, ['dolar', 'udis'], match_field='date'
        )

    def request_data(self, date_start, date_end):
        headers = {'Content-Type': 'application/json', 'Bmx-Token': self.token}
        url = self.get_url(date_start, date_end)
        response = requests.get(url, headers=headers)
        response = response.json()
        return response

    def process_data(self, date_start: date, date_end: date):
        date_start = convert_date_to_str(date_start)
        date_end = convert_date_to_str(date_end)
        # if not queryset.exists():
        data = self.request_data(date_start, date_end)
        self.create_or_update_model(data)
        model_data = self.get_model_data(date_start, date_end)
        return model_data
