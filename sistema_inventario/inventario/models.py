from django.db import models


class Item(models.Model):
	"""Representa un elemento del inventario.

	Campos principales:
	- nombre: nombre del item
	- descripcion: detalle opcional
	- cantidad: stock disponible (no negativo)
	- ubicacion: ubicación física dentro de la bodega
	- fecha_ingreso: fecha en que se creó el registro
	"""

	nombre = models.CharField(max_length=200)
	descripcion = models.TextField(blank=True)
	cantidad = models.PositiveIntegerField(default=0)
	ubicacion = models.CharField(max_length=100, blank=True)
	fecha_ingreso = models.DateField(auto_now_add=True)

	class Meta:
		ordering = ['-fecha_ingreso', 'nombre']

	def __str__(self):
		return f"{self.nombre} ({self.cantidad})"


class Repuesto(models.Model):
	"""Repuestos o insumos relacionados a items.

	- codigo: identificador único del repuesto
	- item_relacionado: FK opcional a un Item (SET_NULL en eliminación)
	- stock: cantidad disponible
	"""

	nombre = models.CharField(max_length=200)
	codigo = models.CharField(max_length=50, unique=True)
	stock = models.PositiveIntegerField(default=0)
	item_relacionado = models.ForeignKey(
		Item,
		null=True,
		blank=True,
		on_delete=models.SET_NULL,
		related_name='repuestos'
	)
	proveedor = models.CharField(max_length=150, blank=True)
	fecha_compra = models.DateField(null=True, blank=True)

	class Meta:
		ordering = ['nombre']

	def __str__(self):
		return f"{self.nombre} [{self.codigo}]"
