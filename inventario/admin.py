from django.contrib import admin
from .models import Categoria, Producto, Sucursal, StockSucursal, MovimientoInventario

class StockSucursalInline(admin.TabularInline):
    model = StockSucursal
    extra = 1

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion']
    search_fields = ['nombre']

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nombre', 'categoria', 'precio', 'stock_actual', 'stock_bajo', 'activo']
    list_filter = ['categoria', 'requiere_receta', 'activo', 'laboratorio']
    search_fields = ['nombre', 'codigo', 'laboratorio', 'principio_activo']
    list_editable = ['stock_actual', 'precio']
    inlines = [StockSucursalInline]
    fieldsets = (
        ('Información Básica', {
            'fields': ('codigo', 'codigo_barras', 'nombre', 'descripcion', 'categoria')
        }),
        ('Precio y Stock', {
            'fields': ('precio', 'stock_actual', 'stock_minimo', 'stock_maximo', 'unidad_medida')
        }),
        ('Detalles Adicionales', {
            'fields': ('laboratorio', 'principio_activo', 'requiere_receta', 'fecha_vencimiento')
        }),
        ('Ubicación y Estado', {
            'fields': ('ubicacion', 'activo', 'imagen')
        }),
    )
    
    def stock_bajo(self, obj):
        return obj.stock_actual <= obj.stock_minimo
    stock_bajo.boolean = True
    stock_bajo.short_description = 'Stock bajo'

@admin.register(Sucursal)
class SucursalAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'direccion', 'telefono', 'activa']
    list_filter = ['activa']
    search_fields = ['nombre', 'direccion']

@admin.register(StockSucursal)
class StockSucursalAdmin(admin.ModelAdmin):
    list_display = ['producto', 'sucursal', 'cantidad', 'fecha_actualizacion']
    list_filter = ['sucursal', 'producto__categoria']
    search_fields = ['producto__nombre', 'sucursal__nombre']

@admin.register(MovimientoInventario)
class MovimientoInventarioAdmin(admin.ModelAdmin):
    list_display = ['fecha', 'producto', 'tipo', 'cantidad', 'usuario']
    list_filter = ['tipo', 'fecha']
    search_fields = ['producto__nombre', 'motivo']
    readonly_fields = ['fecha']