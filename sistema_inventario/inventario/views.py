from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
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


class ItemCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
	model = Item
	fields = ['nombre', 'descripcion', 'cantidad', 'ubicacion']
	template_name = 'inventario/item_form.html'
	success_url = reverse_lazy('inventario:item_list')
	success_message = 'Item creado correctamente.'


class ItemUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
	model = Item
	fields = ['nombre', 'descripcion', 'cantidad', 'ubicacion']
	template_name = 'inventario/item_form.html'
	success_url = reverse_lazy('inventario:item_list')
	success_message = 'Item actualizado correctamente.'


class ItemDeleteView(LoginRequiredMixin, DeleteView):
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


class RepuestoCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
	model = Repuesto
	fields = ['nombre', 'codigo', 'stock', 'item_relacionado', 'proveedor', 'fecha_compra']
	template_name = 'inventario/repuesto_form.html'
	success_url = reverse_lazy('inventario:repuesto_list')
	success_message = 'Repuesto creado correctamente.'


class RepuestoUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
	model = Repuesto
	fields = ['nombre', 'codigo', 'stock', 'item_relacionado', 'proveedor', 'fecha_compra']
	template_name = 'inventario/repuesto_form.html'
	success_url = reverse_lazy('inventario:repuesto_list')
	success_message = 'Repuesto actualizado correctamente.'


class RepuestoDeleteView(LoginRequiredMixin, DeleteView):
	model = Repuesto
	template_name = 'inventario/repuesto_confirm_delete.html'
	success_url = reverse_lazy('inventario:repuesto_list')
