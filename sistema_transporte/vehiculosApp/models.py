from django.db import models
from conductoresApp.models import Conductor


# Create your models here.
class Vehiculo(models.Model):
    modelo = models.CharField('Modelo', max_length=21,null=False)
    placa = models.CharField('Placa',max_length=7, unique=True, null=False)
    capacidad = models.CharField('Capacidad',max_length=7, unique=False)
    conductor_id = models.ForeignKey(Conductor, related_name='vehiculos', on_delete=models.CASCADE, null=True, blank=True, default="")

    def conductor(self):
        return f'{self.conductor_id.nombre} {self.conductor_id.apellido} ({self.conductor_id.id})'

    class Meta:

        verbose_name = 'Vehiculo'
        verbose_name_plural = 'Vehiculos'

        def __str__(self):
            return self.placa