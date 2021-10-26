from django.db import models
from persona.models import Persona

# Create your models here.
class Operario(models.Model):

    oper_persona_id = models.ForeignKey("persona.Persona", on_delete=models.CASCADE)
    oper_codigo = models.CharField(max_length=50)
    oper_especialidad = models.CharField(max_length=50)
    oper_created = models.DateField(auto_now_add=True)
    oper_updated = models.DateField(auto_now=True)

    class Meta:
        verbose_name = ("Operario")
        verbose_name_plural = ("Operarios")

    def _str_(self):
        return self.oper_codigo
