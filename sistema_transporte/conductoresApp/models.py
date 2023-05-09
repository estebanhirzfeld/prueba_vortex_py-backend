from django.db import models


# Create your models here.
class Conductor(models.Model):
    
    identificacion = models.CharField('Identificacion', max_length=11, unique=True, null=False)
    nombre = models.CharField('Nombre',max_length=20, unique=False, null=False)
    apellido = models.CharField('Apellido',max_length=20, unique=False, null= True)
    telefono = models. CharField('Telefono',max_length=10, unique=False, null=False)
    direccion = models.CharField('Direccion',max_length=50, unique=True, null=True)

class Meta:

    verbose_name = 'Conductor'
    verbose_name_prural = 'Conductores'

    def __str__(self):
        return self.identificacion