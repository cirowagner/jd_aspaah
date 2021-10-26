from django.db import models
from socio.models import Socio

# Create your models here.
class Raza(models.Model):

    raza_nombre = models.CharField(max_length=50)
    raza_estado = models.CharField(max_length=2)
    raza_created = models.DateField(auto_now_add=True)
    raza_updated = models.DateField(auto_now=True)

    class Meta:
        verbose_name = ("Raza")
        verbose_name_plural = ("Razas")

    def _str_(self):
        return self.raza_nombre



class Bovino(models.Model):

    bvn_socio_id = models.ForeignKey("socio.Socio", on_delete=models.CASCADE)
    bvn_raza_id = models.ForeignKey("Raza", on_delete=models.CASCADE)
    bvn_nombre = models.CharField(max_length=50)
    bvn_codigo = models.CharField(max_length=50)
    bvn_fnacimiento = models.DateField()
    bvn_genero = models.CharField(max_length=50)
    bvn_estado = models.CharField(max_length=50)
    bvn_created = models.DateField(auto_now_add=True)
    bvn_updated = models.DateField(auto_now=True)

    class Meta:
        verbose_name = ("Bovino")
        verbose_name_plural = ("Bovinos")

    def _str_(self):
        return self.bvn_nombre



class Control_produccion_leche(models.Model):

    cpl_bovino_id = models.ForeignKey("Bovino", on_delete=models.CASCADE)
    cpl_fecha = models.DateField()
    cpl_cantidad = models.CharField(max_length=50)
    cpl_observacion = models.CharField(max_length=50)
    cpl_created = models.DateField(auto_now_add=True)
    cpl_updated = models.DateField(auto_now=True)

    class Meta:
        verbose_name = ("Control_produccion_leche")
        verbose_name_plural = ("Controles_produccion_leche")

    def _str_(self):
        return self.cpl_fecha
