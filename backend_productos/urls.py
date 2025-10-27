from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('categorias/', include('app_productos.urls')),
    path('productos/', include('app_productos.urls')),

    # Redirigir la raíz '/' al listado de productos
    path('', lambda request: redirect('app_productos:listar_productos')),
]
