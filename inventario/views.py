from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.http import JsonResponse
from django.db.models import Q
from .models import Producto, Categoria, Sucursal, StockSucursal
import json

def inicio(request):
    """Vista principal de la app móvil"""
    destacados = Producto.objects.filter(
        activo=True, 
        stock_actual__gt=0
    ).order_by('-fecha_creacion')[:10]
    
    categorias = Categoria.objects.all()
    
    context = {
        'destacados': destacados,
        'categorias': categorias,
    }
    return render(request, 'inicio.html', context)

class CatalogoView(ListView):
    """Vista de catálogo/búsqueda"""
    model = Producto
    template_name = 'catalogo.html'
    context_object_name = 'productos'
    paginate_by = 20
    
    def get_queryset(self):
        queryset = Producto.objects.filter(activo=True)
        
        # Búsqueda por texto
        query = self.request.GET.get('q', '')
        if query:
            queryset = queryset.filter(
                Q(nombre__icontains=query) | 
                Q(laboratorio__icontains=query) |
                Q(descripcion__icontains=query)
            )
        
        # Filtro por categoría
        categoria = self.request.GET.get('categoria')
        if categoria:
            queryset = queryset.filter(categoria_id=categoria)
        
        # Ordenamiento
        orden = self.request.GET.get('orden')
        if orden:
            queryset = queryset.order_by(orden)
        else:
            queryset = queryset.order_by('nombre')
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        context['total_productos'] = self.get_queryset().count()
        context['query'] = self.request.GET.get('q', '')
        return context

class ProductoDetailView(DetailView):
    """Vista de detalle de producto"""
    model = Producto
    template_name = 'producto_detalle.html'
    context_object_name = 'producto'
    
    def get_queryset(self):
        return Producto.objects.filter(activo=True)

def mapa_sucursales(request, producto_id):
    """Vista de mapa con disponibilidad en sucursales"""
    producto = get_object_or_404(Producto, id=producto_id, activo=True)
    
    stocks = StockSucursal.objects.filter(
        producto=producto,
        sucursal__activa=True
    ).select_related('sucursal')
    
    sucursales_data = []
    for stock in stocks:
        sucursales_data.append({
            'nombre': stock.sucursal.nombre,
            'direccion': stock.sucursal.direccion,
            'telefono': stock.sucursal.telefono,
            'cantidad': stock.cantidad,
            'lat': stock.sucursal.latitud,
            'lng': stock.sucursal.longitud,
            'horario': stock.sucursal.horario,
        })
    
    context = {
        'producto': producto,
        'stocks': stocks,
        'sucursales_json': json.dumps(sucursales_data),
        'api_key': 'AIzaSyB41DRUbKWJHPxaFjMAwdrzWzbVKartNGg',  # API key de prueba - cámbiala
    }
    
    return render(request, 'mapa_sucursales.html', context)

def busqueda_api(request):
    """API para búsqueda en tiempo real"""
    query = request.GET.get('q', '')
    if len(query) >= 2:
        productos = Producto.objects.filter(
            Q(nombre__icontains=query) | 
            Q(laboratorio__icontains=query),
            activo=True,
            stock_actual__gt=0
        )[:10]
        
        results = [{
            'id': p.id,
            'nombre': p.nombre,
            'laboratorio': p.laboratorio or 'Genérico',
            'precio': float(p.precio),
            'stock': p.stock_actual,
        } for p in productos]
        
        return JsonResponse({
            'total': len(results),
            'resultados': results
        })
    
    return JsonResponse({'total': 0, 'resultados': []})