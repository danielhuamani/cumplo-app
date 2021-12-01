import os
from django.conf import settings
from datetime import date
from .utils import convert_date_to_str
import requests


class Baxinco:

    def __init__(self):
        self.token = settings.TOKEN
        self.base_url = "https://www.banxico.org.mx/SieAPIRest/service/v1/series/SP68257,SF43718/datos"

    def get_url(self, date_start, date_end):
        return self.base_url + '/{0}/{1}'.format(date_start, date_end)

    def request_data(self, date_start: date, date_end: date):
        date_start = convert_date_to_str(date_start)
        date_end = convert_date_to_str(date_end)
        headers = {'Content-Type': 'application/json', 'Bmx-Token': self.token}
        url = self.get_url(date_start, date_end)
        response = requests.get(url, headers=headers)
        response = response.json()
        print(response)
        return response
