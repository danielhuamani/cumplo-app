from django.db import models


class Banxico(models.Model):
    date = models.DateField()
    udis = models.DecimalField(max_digits=12, decimal_places=8)
    dolar = models.DecimalField(max_digits=12, decimal_places=8)
