from django.urls import path
from . import views

app_name = 'inventario'

urlpatterns = [
    # Item URLs
    path('', views.ItemListView.as_view(), name='item_list'),
    path('item/add/', views.ItemCreateView.as_view(), name='item_add'),
    path('item/<int:pk>/', views.ItemDetailView.as_view(), name='item_detail'),
    path('item/<int:pk>/edit/', views.ItemUpdateView.as_view(), name='item_edit'),
    path('item/<int:pk>/delete/', views.ItemDeleteView.as_view(), name='item_delete'),

    # Repuesto URLs
    path('repuestos/', views.RepuestoListView.as_view(), name='repuesto_list'),
    path('repuesto/add/', views.RepuestoCreateView.as_view(), name='repuesto_add'),
    path('repuesto/<int:pk>/', views.RepuestoDetailView.as_view(), name='repuesto_detail'),
    path('repuesto/<int:pk>/edit/', views.RepuestoUpdateView.as_view(), name='repuesto_edit'),
    path('repuesto/<int:pk>/delete/', views.RepuestoDeleteView.as_view(), name='repuesto_delete'),
]
