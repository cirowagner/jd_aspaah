from django.db import models
from tractor.models import Tractor
from tracto.models import Tracto
from operario.models import Operario


# Create your models here.
class Implemento_agricola(models.Model):

    ia_codigo = models.CharField(max_length=50)
    ia_modelo = models.CharField(max_length=50)
    ia_ancho = models.CharField(max_length=50)
    ia_potencia = models.CharField(max_length=50)
    ia_peso = models.CharField(max_length=50)
    ia_created = models.DateField(auto_now_add=True)
    ia_updated = models.DateField(auto_now=True)

    class Meta:
        verbose_name = ("Ficha_control")
        verbose_name_plural = ("Fichas_control")

    def _str_(self):
        return self.ia_codigo



class Ficha_control(models.Model):

    fc_tractor_id = models.ForeignKey("tractor.Tractor", on_delete=models.CASCADE)
    fc_operario_id = models.ForeignKey("operario.Operario", on_delete=models.CASCADE)
    fc_ia_id = models.ForeignKey("Implemento_agricola", on_delete=models.CASCADE)
    fc_fecha_inicio = models.DateField()
    fc_fecha_fin = models.DateField()

    class Meta:
        verbose_name = ("Ficha_control")
        verbose_name_plural = ("Fichas_control")

    def _str_(self):
        return self.fc_fecha_inicio



class Detalle_ficha_control(models.Model):

    dfc_tracto_id = models.ForeignKey("tracto.Tracto", on_delete=models.CASCADE)
    dfc_fc_id = models.ForeignKey("Ficha_control", on_delete=models.CASCADE)
    dfc_observaciones = models.CharField(max_length=50)
    dfc_importe = models.CharField(max_length=50)
    dfc_created = models.DateField(auto_now_add=True)
    dfc_updated = models.DateField(auto_now=True)

    class Meta:
        verbose_name = ("Detalle_ficha_control")
        verbose_name_plural = ("Detalles_ficha_control")

    def _str_(self):
        return self.dfc_observaciones
