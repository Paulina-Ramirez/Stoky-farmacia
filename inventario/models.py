from django.db import models
from django.utils import timezone

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)
    icono = models.CharField(max_length=50, blank=True, help_text='Nombre del icono (FontAwesome)')
    
    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ['nombre']
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    UNIDADES = [
        ('tableta', 'Tableta'),
        ('caja', 'Caja'),
        ('frasco', 'Frasco'),
        ('ampolla', 'Ampolla'),
        ('ml', 'Mililitros'),
        ('g', 'Gramos'),
        ('pieza', 'Pieza'),
    ]
    
    codigo = models.CharField('Código', max_length=50, unique=True)
    codigo_barras = models.CharField('Código de barras', max_length=100, blank=True)
    nombre = models.CharField('Nombre', max_length=200)
    descripcion = models.TextField('Descripción', blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    precio = models.DecimalField('Precio', max_digits=10, decimal_places=2)
    stock_actual = models.IntegerField('Stock actual', default=0)
    stock_minimo = models.IntegerField('Stock mínimo', default=5)
    stock_maximo = models.IntegerField('Stock máximo', default=100)
    unidad_medida = models.CharField('Unidad de medida', max_length=20, choices=UNIDADES, default='tableta')
    requiere_receta = models.BooleanField('Requiere receta', default=False)
    laboratorio = models.CharField('Laboratorio', max_length=100, blank=True)
    principio_activo = models.CharField('Principio activo', max_length=200, blank=True)
    fecha_vencimiento = models.DateField('Fecha de vencimiento', null=True, blank=True)
    ubicacion = models.CharField('Ubicación', max_length=50, blank=True)
    activo = models.BooleanField('Activo', default=True)
    imagen = models.ImageField('Imagen', upload_to='productos/', null=True, blank=True)
    fecha_creacion = models.DateTimeField('Fecha creación', auto_now_add=True)
    fecha_actualizacion = models.DateTimeField('Fecha actualización', auto_now=True)
    
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['nombre']
    
    def __str__(self):
        return f"{self.nombre} - {self.stock_actual} {self.get_unidad_medida_display()}"
    
    @property
    def stock_bajo(self):
        return self.stock_actual <= self.stock_minimo
    
    @property
    def disponible(self):
        return self.stock_actual > 0 and self.activo

class Sucursal(models.Model):
    nombre = models.CharField('Nombre', max_length=100)
    direccion = models.TextField('Dirección')
    telefono = models.CharField('Teléfono', max_length=20, blank=True)
    latitud = models.FloatField('Latitud', null=True, blank=True)
    longitud = models.FloatField('Longitud', null=True, blank=True)
    horario = models.CharField('Horario', max_length=200, blank=True)
    activa = models.BooleanField('Activa', default=True)
    
    class Meta:
        verbose_name = "Sucursal"
        verbose_name_plural = "Sucursales"
    
    def __str__(self):
        return self.nombre

class StockSucursal(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='stock_sucursales')
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    cantidad = models.IntegerField('Cantidad', default=0)
    fecha_actualizacion = models.DateTimeField('Última actualización', auto_now=True)
    
    class Meta:
        verbose_name = "Stock por sucursal"
        verbose_name_plural = "Stocks por sucursal"
        unique_together = ['producto', 'sucursal']
    
    def __str__(self):
        return f"{self.producto.nombre} - {self.sucursal.nombre}: {self.cantidad}"

class MovimientoInventario(models.Model):
    TIPO_MOVIMIENTO = [
        ('entrada', 'Entrada'),
        ('salida', 'Salida'),
        ('ajuste', 'Ajuste'),
    ]
    
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    tipo = models.CharField('Tipo', max_length=20, choices=TIPO_MOVIMIENTO)
    cantidad = models.IntegerField('Cantidad')
    stock_anterior = models.IntegerField()
    stock_nuevo = models.IntegerField()
    motivo = models.TextField('Motivo', blank=True)
    usuario = models.CharField(max_length=100, blank=True)
    fecha = models.DateTimeField('Fecha', auto_now_add=True)
    
    class Meta:
        verbose_name = "Movimiento de inventario"
        verbose_name_plural = "Movimientos de inventario"
        ordering = ['-fecha']
    
    def __str__(self):
        return f"{self.get_tipo_display()} - {self.producto.nombre} - {self.cantidad}"