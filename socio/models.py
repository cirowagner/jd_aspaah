from django.db import models
from persona.models import Persona

# Create your models here.
class Ubicacion(models.Model):

    ubic_departamento = models.CharField(max_length=50)
    ubic_provincia = models.CharField(max_length=50)
    ubic_distrito = models.CharField(max_length=50)
    ubic_comunidad = models.CharField(max_length=50)
    ubic_created = models.DateField(auto_now_add=True)
    ubic_updated = models.DateField(auto_now=True)

    class Meta:
        verbose_name = ("Ubicacion")
        verbose_name_plural = ("Ubicaciones")

    def _str_(self):
        return self.ubic_departamento

class Socio(models.Model):

    socio_persona_id = models.ForeignKey("persona.Persona", on_delete=models.CASCADE)
    parent_socio_id = models.ForeignKey("Socio", on_delete=models.CASCADE)
    socio_codigo = models.CharField(max_length=50)
    socio_categoria = models.CharField(max_length=50)
    socio_tipo = models.CharField(max_length=50)
    socio_parentesco = models.CharField(max_length=50)
    socio_estado = models.CharField(max_length=50)
    socio_ubic = models.ForeignKey("Ubicacion", on_delete=models.CASCADE)
    socio_created = models.DateField(auto_now_add=True)
    socio_updated = models.DateField(auto_now=True)

    class Meta:
        verbose_name = ("Socio")
        verbose_name_plural = ("Socios")

    def _str_(self):
        return self.socio_codigo
