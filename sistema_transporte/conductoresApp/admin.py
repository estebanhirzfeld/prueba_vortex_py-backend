from django.contrib import admin
from conductoresApp.models import Conductor

# Register your models here.

class ConductorAdmin(admin.ModelAdmin):
    search_fields = ('nombre', 'apellido', 'identificacion', 'telefono', 'direccion')
    list_display = ('nombre', 'apellido', 'identificacion', 'telefono', 'direccion')

admin.site.register(Conductor, ConductorAdmin)
