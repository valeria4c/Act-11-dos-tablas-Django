from django.contrib import admin
from .models import Categorias, Productos  # <- eliminar Proveedor

# Registrar tus modelos en el admin
admin.site.register(Categorias)
admin.site.register(Productos)
