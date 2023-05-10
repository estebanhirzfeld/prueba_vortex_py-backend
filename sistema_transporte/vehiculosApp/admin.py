from django.contrib import admin
from vehiculosApp.models import Vehiculo

# Register your models here.

class VehiculoAdmin(admin.ModelAdmin):
    # modelo, placa, capacidad, conductor_id
    search_fields = ('placa',  'conductor_id', 'modelo', 'capacidad',)
    list_display = ('placa', 'conductor', 'modelo', 'capacidad', )
    raw_id_fields = ('conductor_id',)


admin.site.register(Vehiculo, VehiculoAdmin)

