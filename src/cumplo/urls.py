from django.urls import path
from .views import UdisView, DolarView

urlpatterns = [
    path('', UdisView.as_view(), name='udis'),
    path('dolar', DolarView.as_view(), name='dolar'),
]
