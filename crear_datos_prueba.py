# crear_datos_prueba.py
import os
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from inventario.models import Categoria, Producto, Sucursal, StockSucursal
from datetime import date, timedelta
import random

def crear_datos():
    print("🚀 Creando datos de prueba...")
    
    # 1. CREAR CATEGORÍAS
    print("📁 Creando categorías...")
    categorias_data = [
        {'nombre': 'Analgésicos', 'descripcion': 'Medicamentos para aliviar el dolor', 'icono': '💊'},
        {'nombre': 'Antibióticos', 'descripcion': 'Medicamentos para infecciones bacterianas', 'icono': '🔬'},
        {'nombre': 'Antiinflamatorios', 'descripcion': 'Reducen la inflamación', 'icono': '🩹'},
        {'nombre': 'Antialérgicos', 'descripcion': 'Para alergias y reacciones alérgicas', 'icono': '🌸'},
        {'nombre': 'Gastrointestinales', 'descripcion': 'Para problemas estomacales', 'icono': '🍽️'},
        {'nombre': 'Cardiovasculares', 'descripcion': 'Para el corazón y circulación', 'icono': '❤️'},
        {'nombre': 'Vitaminas', 'descripcion': 'Suplementos vitamínicos', 'icono': '💪'},
        {'nombre': 'Cuidado Personal', 'descripcion': 'Productos de higiene y cuidado', 'icono': '🧴'},
        {'nombre': 'Primeros Auxilios', 'descripcion': 'Material de curación', 'icono': '🏥'},
        {'nombre': 'Infantil', 'descripcion': 'Productos para niños', 'icono': '👶'},
    ]
    
    categorias = {}
    for cat_data in categorias_data:
        cat, created = Categoria.objects.get_or_create(
            nombre=cat_data['nombre'],
            defaults={
                'descripcion': cat_data['descripcion'],
                'icono': cat_data['icono']
            }
        )
        categorias[cat.nombre] = cat
        print(f"  {'✅' if created else '🔄'} {cat.nombre}")
    
    # 2. CREAR SUCURSALES
    print("\n🏢 Creando sucursales...")
    sucursales_data = [
        {
            'nombre': 'Stoky Centro',
            'direccion': 'Av. Reforma 123, Col. Centro, CDMX',
            'telefono': '55-1234-5678',
            'latitud': 19.4326,
            'longitud': -99.1332,
            'horario': 'Lun-Vie 8:00-21:00, Sáb-Dom 9:00-19:00',
        },
        {
            'nombre': 'Stoky Norte',
            'direccion': 'Av. Insurgentes Norte 456, Col. Lindavista, CDMX',
            'telefono': '55-2345-6789',
            'latitud': 19.4850,
            'longitud': -99.1200,
            'horario': 'Lun-Dom 8:00-22:00',
        },
        {
            'nombre': 'Stoky Sur',
            'direccion': 'Av. Universidad 789, Col. Del Valle, CDMX',
            'telefono': '55-3456-7890',
            'latitud': 19.3820,
            'longitud': -99.1690,
            'horario': 'Lun-Vie 9:00-21:00, Sáb 9:00-20:00',
        },
        {
            'nombre': 'Stoky Poniente',
            'direccion': 'Av. Santa Fe 234, Col. Santa Fe, CDMX',
            'telefono': '55-4567-8901',
            'latitud': 19.3580,
            'longitud': -99.2590,
            'horario': 'Lun-Sáb 8:00-21:00, Dom 10:00-18:00',
        },
        {
            'nombre': 'Stoky Oriente',
            'direccion': 'Av. Zaragoza 567, Col. Iztapalapa, CDMX',
            'telefono': '55-5678-9012',
            'latitud': 19.3950,
            'longitud': -99.0950,
            'horario': 'Lun-Dom 8:00-20:00',
        },
    ]
    
    sucursales = []
    for suc_data in sucursales_data:
        suc, created = Sucursal.objects.get_or_create(
            nombre=suc_data['nombre'],
            defaults={
                'direccion': suc_data['direccion'],
                'telefono': suc_data['telefono'],
                'latitud': suc_data['latitud'],
                'longitud': suc_data['longitud'],
                'horario': suc_data['horario'],
                'activa': True
            }
        )
        sucursales.append(suc)
        print(f"  {'✅' if created else '🔄'} {suc.nombre}")
    
    # 3. CREAR PRODUCTOS
    print("\n📦 Creando productos...")
    
    productos_data = [
        # Analgésicos
        {'codigo': 'ANA001', 'nombre': 'Paracetamol 500mg', 'laboratorio': 'Genérico', 'precio': 18.50, 'stock': 150, 'categoria': 'Analgésicos', 'unidad': 'tableta', 'requiere_receta': False},
        {'codigo': 'ANA002', 'nombre': 'Ibuprofeno 400mg', 'laboratorio': 'Genérico', 'precio': 22.00, 'stock': 12, 'categoria': 'Analgésicos', 'unidad': 'tableta', 'requiere_receta': False},
        {'codigo': 'ANA003', 'nombre': 'Naproxeno 250mg', 'laboratorio': 'Bayer', 'precio': 35.50, 'stock': 45, 'categoria': 'Analgésicos', 'unidad': 'tableta', 'requiere_receta': False},
        {'codigo': 'ANA004', 'nombre': 'Ketorolaco 30mg', 'laboratorio': 'Rimsa', 'precio': 42.00, 'stock': 30, 'categoria': 'Analgésicos', 'unidad': 'ampolla', 'requiere_receta': True},
        
        # Antibióticos
        {'codigo': 'ANT001', 'nombre': 'Amoxicilina 500mg', 'laboratorio': 'Genérico', 'precio': 28.50, 'stock': 80, 'categoria': 'Antibióticos', 'unidad': 'cápsula', 'requiere_receta': True},
        {'codigo': 'ANT002', 'nombre': 'Azitromicina 500mg', 'laboratorio': 'Pfizer', 'precio': 65.00, 'stock': 25, 'categoria': 'Antibióticos', 'unidad': 'tableta', 'requiere_receta': True},
        {'codigo': 'ANT003', 'nombre': 'Ciprofloxacino 250mg', 'laboratorio': 'Bayer', 'precio': 45.50, 'stock': 40, 'categoria': 'Antibióticos', 'unidad': 'tableta', 'requiere_receta': True},
        
        # Antiinflamatorios
        {'codigo': 'AIF001', 'nombre': 'Diclofenaco 100mg', 'laboratorio': 'Novartis', 'precio': 25.00, 'stock': 60, 'categoria': 'Antiinflamatorios', 'unidad': 'tableta', 'requiere_receta': False},
        {'codigo': 'AIF002', 'nombre': 'Meloxicam 15mg', 'laboratorio': 'Boehringer', 'precio': 38.00, 'stock': 35, 'categoria': 'Antiinflamatorios', 'unidad': 'tableta', 'requiere_receta': True},
        
        # Antialérgicos
        {'codigo': 'ALE001', 'nombre': 'Loratadina 10mg', 'laboratorio': 'Bayer', 'precio': 15.50, 'stock': 200, 'categoria': 'Antialérgicos', 'unidad': 'tableta', 'requiere_receta': False},
        {'codigo': 'ALE002', 'nombre': 'Cetirizina 10mg', 'laboratorio': 'GSK', 'precio': 16.00, 'stock': 180, 'categoria': 'Antialérgicos', 'unidad': 'tableta', 'requiere_receta': False},
        {'codigo': 'ALE003', 'nombre': 'Desloratadina 5mg', 'laboratorio': 'MSD', 'precio': 42.00, 'stock': 50, 'categoria': 'Antialérgicos', 'unidad': 'tableta', 'requiere_receta': False},
        
        # Gastrointestinales
        {'codigo': 'GAS001', 'nombre': 'Omeprazol 20mg', 'laboratorio': 'Genérico', 'precio': 19.00, 'stock': 120, 'categoria': 'Gastrointestinales', 'unidad': 'cápsula', 'requiere_receta': False},
        {'codigo': 'GAS002', 'nombre': 'Ranitidina 150mg', 'laboratorio': 'GSK', 'precio': 22.50, 'stock': 90, 'categoria': 'Gastrointestinales', 'unidad': 'tableta', 'requiere_receta': False},
        {'codigo': 'GAS003', 'nombre': 'Hioscina 10mg', 'laboratorio': 'Boehringer', 'precio': 28.00, 'stock': 75, 'categoria': 'Gastrointestinales', 'unidad': 'tableta', 'requiere_receta': False},
        
        # Vitaminas
        {'codigo': 'VIT001', 'nombre': 'Vitamina C 1000mg', 'laboratorio': 'Bayer', 'precio': 35.00, 'stock': 300, 'categoria': 'Vitaminas', 'unidad': 'tableta', 'requiere_receta': False},
        {'codigo': 'VIT002', 'nombre': 'Complejo B', 'laboratorio': 'Abbott', 'precio': 42.00, 'stock': 150, 'categoria': 'Vitaminas', 'unidad': 'tableta', 'requiere_receta': False},
        {'codigo': 'VIT003', 'nombre': 'Vitamina D 400 UI', 'laboratorio': 'Pfizer', 'precio': 28.50, 'stock': 200, 'categoria': 'Vitaminas', 'unidad': 'cápsula', 'requiere_receta': False},
        
        # Cuidado Personal
        {'codigo': 'CUI001', 'nombre': 'Jabón Antibacterial', 'laboratorio': 'Palmolive', 'precio': 25.00, 'stock': 200, 'categoria': 'Cuidado Personal', 'unidad': 'ml', 'requiere_receta': False},
        {'codigo': 'CUI002', 'nombre': 'Alcohol en Gel', 'laboratorio': 'Dettol', 'precio': 42.00, 'stock': 150, 'categoria': 'Cuidado Personal', 'unidad': 'ml', 'requiere_receta': False},
        {'codigo': 'CUI003', 'nombre': 'Cubrebocas KN95', 'laboratorio': '3M', 'precio': 15.00, 'stock': 500, 'categoria': 'Cuidado Personal', 'unidad': 'pieza', 'requiere_receta': False},
        {'codigo': 'CUI004', 'nombre': 'Gel Antibacterial', 'laboratorio': 'Dettol', 'precio': 35.00, 'stock': 180, 'categoria': 'Cuidado Personal', 'unidad': 'ml', 'requiere_receta': False},
        
        # Primeros Auxilios
        {'codigo': 'AUX001', 'nombre': 'Curitas adhesivas', 'laboratorio': '3M', 'precio': 25.00, 'stock': 400, 'categoria': 'Primeros Auxilios', 'unidad': 'caja', 'requiere_receta': False},
        {'codigo': 'AUX002', 'nombre': 'Gasa estéril 10x10', 'laboratorio': 'Kimberly', 'precio': 18.00, 'stock': 300, 'categoria': 'Primeros Auxilios', 'unidad': 'pieza', 'requiere_receta': False},
        {'codigo': 'AUX003', 'nombre': 'Venda elástica', 'laboratorio': '3M', 'precio': 22.00, 'stock': 250, 'categoria': 'Primeros Auxilios', 'unidad': 'pieza', 'requiere_receta': False},
        
        # Infantil
        {'codigo': 'INF001', 'nombre': 'Paracetamol infantil 100mg/ml', 'laboratorio': 'Genérico', 'precio': 45.00, 'stock': 80, 'categoria': 'Infantil', 'unidad': 'frasco', 'requiere_receta': False},
        {'codigo': 'INF002', 'nombre': 'Ibuprofeno infantil 100mg/5ml', 'laboratorio': 'Pfizer', 'precio': 52.00, 'stock': 60, 'categoria': 'Infantil', 'unidad': 'frasco', 'requiere_receta': False},
    ]
    
    productos_creados = []
    for prod_data in productos_data:
        categoria = categorias[prod_data['categoria']]
        
        # Fecha de vencimiento aleatoria (entre 6 meses y 2 años)
        dias = random.randint(180, 730)
        fecha_venc = date.today() + timedelta(days=dias)
        
        prod, created = Producto.objects.get_or_create(
            codigo=prod_data['codigo'],
            defaults={
                'nombre': prod_data['nombre'],
                'categoria': categoria,
                'precio': prod_data['precio'],
                'stock_actual': prod_data['stock'],
                'stock_minimo': random.randint(5, 20),
                'laboratorio': prod_data['laboratorio'],
                'unidad_medida': prod_data['unidad'],
                'requiere_receta': prod_data['requiere_receta'],
                'descripcion': f"{prod_data['nombre']} - {prod_data['laboratorio']}",
                'fecha_vencimiento': fecha_venc,
                'activo': True,
                'ubicacion': f"Estante {random.choice('ABCDEFGH')}{random.randint(1,20)}"
            }
        )
        productos_creados.append(prod)
        print(f"  {'✅' if created else '🔄'} {prod.nombre}")
    
    # 4. CREAR STOCK EN SUCURSALES
    print("\n📊 Distribuyendo stock en sucursales...")
    
    contador = 0
    for producto in productos_creados:
        for sucursal in sucursales:
            # Cantidad aleatoria pero proporcional al stock total
            if producto.stock_actual > 0:
                cantidad = max(0, int(random.gauss(producto.stock_actual / len(sucursales), 10)))
                cantidad = max(0, min(producto.stock_actual, cantidad))
                
                StockSucursal.objects.get_or_create(
                    producto=producto,
                    sucursal=sucursal,
                    defaults={'cantidad': cantidad}
                )
                contador += 1
    
    # 5. MOSTRAR RESUMEN
    print("\n" + "="*50)
    print("✅ ¡DATOS CREADOS EXITOSAMENTE!")
    print("="*50)
    print(f"📁 Categorías: {Categoria.objects.count()}")
    print(f"📦 Productos: {Producto.objects.count()}")
    print(f"🏢 Sucursales: {Sucursal.objects.count()}")
    print(f"📊 Stock en sucursales: {StockSucursal.objects.count()}")
    print("="*50)
    print("\n🔍 Para probar:")
    print("  • Admin: http://127.0.0.1:8000/admin/")
    print("  • App: http://127.0.0.1:8000/")
    print("="*50)

if __name__ == '__main__':
    crear_datos()