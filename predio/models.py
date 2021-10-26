from django.db import models
from socio.models import Socio

# Create your models here.
class Semilla(models.Model):

    sem_nombre = models.CharField(max_length=50)
    sem_marca = models.CharField(max_length=50)
    sem_calidad = models.CharField(max_length=50)
    sem_procedencia = models.CharField(max_length=50)
    sem_descripcion = models.CharField(max_length=50)
    sem_created = models.DateField(auto_now_add=True)
    sem_updated = models.DateField(auto_now=True)

    class Meta:
        verbose_name = ("Semilla")
        verbose_name_plural = ("Semillas")

    def _str_(self):
        return self.sem_nombre



class Tipo_forraje(models.Model):

    tf_semilla_id = models.ForeignKey("Semilla", on_delete=models.CASCADE)
    tf_nombre = models.CharField(max_length=50)
    tf_created = models.DateField(auto_now_add=True)
    tf_updated = models.DateField(auto_now=True)

    class Meta:
        verbose_name = ("Tipo_forraje")
        verbose_name_plural = ("Tipos_forrajes")

    def _str_(self):
        return self.tf_nombre



class Predio(models.Model):

    pred_socio_id = models.ForeignKey("socio.Socio", on_delete=models.CASCADE)
    pred_area_total = models.CharField(max_length=50)
    pred_area_pasiva = models.CharField(max_length=50)
    pred_created = models.DateField(auto_now_add=True)
    pred_updated = models.DateField(auto_now=True)

    class Meta:
        verbose_name = ("Predio")
        verbose_name_plural = ("Predios")

    def _str_(self):
        return self.pred_area_total



class Area_operante(models.Model):

    ao_predio_id = models.ForeignKey("Predio", on_delete=models.CASCADE)
    ao_hectareas = models.CharField(max_length=50)
    ao_created = models.DateField(auto_now_add=True)
    ao_updated = models.DateField(auto_now=True)

    class Meta:
        verbose_name = ("Area_operante")
        verbose_name_plural = ("Areas_operantes")

    def _str_(self):
        return self.ao_hectareas



class Detalle_area_operante(models.Model):

    dao_ao_id = models.ForeignKey("Area_operante", on_delete=models.CASCADE)
    dao_tf_id = models.ForeignKey("Tipo_forraje", on_delete=models.CASCADE)
    dao_inicio = models.DateField()
    dao_fin = models.DateField()
    dao_created = models.DateField(auto_now_add=True)
    dao_updated = models.DateField(auto_now=True)

    class Meta:
        verbose_name = ("Detalle_area_operante")
        verbose_name_plural = ("Detalles_areas_operantes")

    def _str_(self):
        return self.dao_inicio