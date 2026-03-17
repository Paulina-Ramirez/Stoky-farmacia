import pandas as pd
from django.core.management.base import BaseCommand
from inventario.models import Producto
from datetime import datetime

class Command(BaseCommand):
    help = 'Exporta inventario a Excel'
    
    def handle(self, *args, **options):
        productos = Producto.objects.all()
        
        data = [{
            'Código': p.codigo,
            'Nombre': p.nombre,
            'Categoría': p.categoria.nombre if p.categoria else '',
            'Stock': p.stock_actual,
            'Precio': p.precio,
            'Laboratorio': p.laboratorio,
        } for p in productos]
        
        df = pd.DataFrame(data)
        filename = f'inventario_{datetime.now().strftime("%Y%m%d")}.xlsx'
        df.to_excel(filename, index=False)
        
        self.stdout.write(self.style.SUCCESS(f'Exportado a {filename}'))