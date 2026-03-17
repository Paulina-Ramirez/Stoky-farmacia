import pandas as pd
from django.core.management.base import BaseCommand
from inventario.models import Producto, Categoria

class Command(BaseCommand):
    help = 'Importa productos desde archivo Excel'
    
    def add_arguments(self, parser):
        parser.add_argument('archivo', type=str)
    
    def handle(self, *args, **options):
        archivo = options['archivo']
        df = pd.read_excel(archivo)
        
        for _, row in df.iterrows():
            categoria, _ = Categoria.objects.get_or_create(
                nombre=row.get('categoria', 'General')
            )
            
            Producto.objects.update_or_create(
                codigo=str(row['codigo']),
                defaults={
                    'nombre': row['nombre'],
                    'categoria': categoria,
                    'precio': float(row['precio']),
                    'stock_actual': int(row['stock']),
                    'laboratorio': row.get('laboratorio', ''),
                }
            )
        
        self.stdout.write(self.style.SUCCESS('Importación completada'))