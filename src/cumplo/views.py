from django.shortcuts import render
from django.views.generic import TemplateView
from .services_layer import BaxincoService
from .utils import get_last_week, convert_str_to_date
# Create your views here.


class UdisView(TemplateView):
    template_name = 'udis.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        date_start = self.request.GET.get('date_start')
        date_end = self.request.GET.get('date_end')
        if date_start and date_end:
            date_start = convert_str_to_date(
                string=date_start, format_date='%Y-%m-%d')
            date_end = convert_str_to_date(
                string=date_end, format_date='%Y-%m-%d')
        else:
            date_start, date_end = get_last_week()
        baxinco = BaxincoService()
        data = baxinco.process_data(date_start, date_end)
        context.update({
            'date_start': date_start,
            'date_end': date_end,
            'data': data
        })
        return context


class DolarView(TemplateView):
    template_name = 'dolar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        date_start = self.request.GET.get('date_start')
        date_end = self.request.GET.get('date_end')
        if date_start and date_end:
            date_start = convert_str_to_date(
                string=date_start, format_date='%Y-%m-%d')
            date_end = convert_str_to_date(
                string=date_end, format_date='%Y-%m-%d')
        else:
            date_start, date_end = get_last_week()
        baxinco = BaxincoService()
        data = baxinco.process_data(date_start, date_end)
        context.update({
            'date_start': date_start,
            'date_end': date_end,
            'data': data
        })
        return context
