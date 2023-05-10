from django.db import models
from conductoresApp.models import Conductor

# Create your models here.
class Pedido(models.Model):
    id = models.IntegerField(primary_key=True)
    # tipo_pedido = models.CharField('Tipo', max_length=20)
    direccion = models.CharField('Direccion',max_length=50,null=False)
    conductor_id = models.ForeignKey(Conductor, related_name='pedidos', on_delete=models.CASCADE, null=False, blank=True, default="")
    fecha = models.DateField('Fecha', auto_now=False, auto_now_add=False, null=False)
    hora = models.TimeField('Hora', auto_now=False, auto_now_add=False, null=False)

    # Tipos de pedido
    TIPO_PEDIDO = (
        ('Mercancia', 'Mercancia'),
        ('Pasajero', 'Pasajero'),
    )
    tipo_pedido = models.CharField('Tipo', max_length=20, choices=TIPO_PEDIDO, default='Mercancia')

    # Estados del pedido
    ESTADO_PEDIDO = (
        ('Pendiente', 'Pendiente'),
        ('En camino', 'En camino'),
        ('Entregado', 'Entregado'),
    )
    estado = models.CharField('Estado', max_length=20, choices=ESTADO_PEDIDO, default='Pendiente')

    def conductor(self):
        return f'{self.conductor_id.nombre} {self.conductor_id.apellido} ({self.conductor_id.id})'

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

        def __str__(self):
            return self.id