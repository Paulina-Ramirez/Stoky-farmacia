from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('catalogo/', views.CatalogoView.as_view(), name='catalogo'),
    path('producto/<int:pk>/', views.ProductoDetailView.as_view(), name='producto_detalle'),
    path('producto/<int:producto_id>/mapa/', views.mapa_sucursales, name='mapa_sucursales'),
    path('api/buscar/', views.busqueda_api, name='busqueda_api'),
]