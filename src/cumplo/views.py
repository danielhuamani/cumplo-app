from django.shortcuts import render
from django.views.generic import TemplateView
from .services_layer import Baxinco
from .utils import get_last_week
# Create your views here.


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        date_start, date_end = get_last_week()
        baxinco = Baxinco()
        baxinco.request_data(date_start, date_end)
        context.update({
            'date_start': date_start,
            'date_end': date_end
        })
        return context
