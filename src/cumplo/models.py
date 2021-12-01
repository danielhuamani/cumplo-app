from django.db import models
from bulk_update_or_create import BulkUpdateOrCreateQuerySet


class BanxicoModel(models.Model):
    date = models.DateField()
    udis = models.DecimalField(max_digits=12, decimal_places=8)
    dolar = models.DecimalField(max_digits=12, decimal_places=8)

    objects = BulkUpdateOrCreateQuerySet.as_manager()
