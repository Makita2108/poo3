from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
	ListView, DetailView, CreateView, UpdateView, DeleteView
)
from .models import Item, Repuesto


# Item views
class ItemListView(ListView):
	model = Item
	template_name = 'inventario/item_list.html'
	context_object_name = 'items'


class ItemDetailView(DetailView):
	model = Item
	template_name = 'inventario/item_detail.html'
	context_object_name = 'item'


class ItemCreateView(CreateView):
	model = Item
	fields = ['nombre', 'descripcion', 'cantidad', 'ubicacion']
	template_name = 'inventario/item_form.html'
	success_url = reverse_lazy('inventario:item_list')


class ItemUpdateView(UpdateView):
	model = Item
	fields = ['nombre', 'descripcion', 'cantidad', 'ubicacion']
	template_name = 'inventario/item_form.html'
	success_url = reverse_lazy('inventario:item_list')


class ItemDeleteView(DeleteView):
	model = Item
	template_name = 'inventario/item_confirm_delete.html'
	success_url = reverse_lazy('inventario:item_list')


# Repuesto views
class RepuestoListView(ListView):
	model = Repuesto
	template_name = 'inventario/repuesto_list.html'
	context_object_name = 'repuestos'


class RepuestoDetailView(DetailView):
	model = Repuesto
	template_name = 'inventario/repuesto_detail.html'
	context_object_name = 'repuesto'


class RepuestoCreateView(CreateView):
	model = Repuesto
	fields = ['nombre', 'codigo', 'stock', 'item_relacionado', 'proveedor', 'fecha_compra']
	template_name = 'inventario/repuesto_form.html'
	success_url = reverse_lazy('inventario:repuesto_list')


class RepuestoUpdateView(UpdateView):
	model = Repuesto
	fields = ['nombre', 'codigo', 'stock', 'item_relacionado', 'proveedor', 'fecha_compra']
	template_name = 'inventario/repuesto_form.html'
	success_url = reverse_lazy('inventario:repuesto_list')


class RepuestoDeleteView(DeleteView):
	model = Repuesto
	template_name = 'inventario/repuesto_confirm_delete.html'
	success_url = reverse_lazy('inventario:repuesto_list')
