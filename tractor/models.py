from django.db import models

# Create your models here.
class Tractor(models.Model):

    tractor_codigo = models.CharField(max_length=50)
    tractor_marca = models.CharField(max_length=50)
    tractor_modelo = models.CharField(max_length=50)
    tractor_potencia = models.CharField(max_length=50)
    tractor_velocidad = models.CharField(max_length=50)
    tractor_articulacion = models.CharField(max_length=50)
    tractor_estado = models.CharField(max_length=2)
    tractor_created = models.DateField(auto_now_add=True)
    tractor_updated = models.DateField(auto_now=True)

    class Meta:
        verbose_name = ("Tractor")
        verbose_name_plural = ("Tractores")

    def _str_(self):
        return self.tractor_codigo
