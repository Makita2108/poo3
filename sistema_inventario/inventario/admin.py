from django.contrib import admin
from .models import Item, Repuesto


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'cantidad', 'ubicacion', 'fecha_ingreso')
	search_fields = ('nombre', 'descripcion', 'ubicacion')


@admin.register(Repuesto)
class RepuestoAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'codigo', 'stock', 'proveedor')
	search_fields = ('nombre', 'codigo', 'proveedor')
