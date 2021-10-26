from django.db import models

# Create your models here.
class Persona(models.Model):

    pers_nombre = models.CharField(max_length=50)
    pers_ap_paterno = models.CharField(max_length=50)
    pers_ap_matenor = models.CharField(max_length=50)
    pers_dni = models.CharField(max_length=8)
    pers_fnacimiento = models.DateField()
    pers_estado_civil = models.CharField(max_length=50)
    pers_sexo = models.CharField(max_length=2)
    pers_telefono = models.CharField(max_length=9)
    pers_correo = models.EmailField(max_length=50)
    pers_direccion = models.CharField(max_length=50)
    pers_nacionalidad = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("Persona")
        verbose_name_plural = ("Personas")

    def _str_(self):
        return self.pers_nombre