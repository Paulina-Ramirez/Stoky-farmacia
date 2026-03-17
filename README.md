# Stoky - Sistema de Inventario para Farmacia

Aplicación web para consultar disponibilidad de productos en farmacias, con vista para usuarios y panel de administración.

## Características

- 📱 **Diseño mobile-first** (optimizado para teléfonos)
- 🔍 **Búsqueda en tiempo real** de productos
- 📦 **Catálogo** con filtros por categoría
- 🗺️ **Mapa de sucursales** con disponibilidad
- 👑 **Panel de administración** para gestión de inventario
- 📊 **Importación/Exportación** desde Excel

## Tecnologías

- Python 3.13+
- Django 6.0+
- Bootstrap 5
- SQLite3
- Pandas (para Excel)


## 🚀 Instalación

### Requisitos Previos
- Python 3.13 o superior
- Git
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/Paulina-Ramirez/Stoky-farmacia.git
   cd Stoky-farmacia

2. **Crear y clonar repositorio**
   # Windows
    python -m venv venv
    venv\Scripts\activate
   
4. **Instalar dependencias**
   pip install -r requirements.txt

5. **Configurar la base de datos**
   python manage.py migrate

6. **Correr el servidor**
   python manage.py runserver
