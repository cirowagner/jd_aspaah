from django.db import models
from socio.models import Socio

# Create your models here.
class Tracto(models.Model):

    tracto_socio_id = models.ForeignKey("socio.Socio", on_delete=models.CASCADE)
    tracto_fecha = models.DateField()
    tracto_horas = models.CharField(max_length=50)
    tracto_tipo = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("Tracto")
        verbose_name_plural = ("Tractos")

    def _str_(self):
        return self.tracto_tipo
