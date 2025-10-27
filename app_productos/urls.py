from django.urls import path
from . import views

app_name = 'app_productos'

urlpatterns = [
    # Categorías
    path('categorias/', views.listar_categorias, name='listar_categorias'),
    path('categorias/nueva/', views.crear_categoria, name='crear_categoria'),
    path('categorias/editar/<int:id>/', views.editar_categoria, name='editar_categoria'),
    path('categorias/eliminar/<int:id>/', views.eliminar_categoria, name='eliminar_categoria'),
    path('categorias/detalle/<int:id>/', views.detalle_categoria, name='detalle_categoria'),


    # Productos
    path('productos/', views.listar_productos, name='listar_productos'),
    path('productos/nuevo/', views.crear_producto, name='crear_producto'),
    path('productos/editar/<int:id>/', views.editar_producto, name='editar_producto'),
    path('productos/eliminar/<int:id>/', views.eliminar_producto, name='eliminar_producto'),
    path('productos/detalle/<int:id>/', views.detalle_producto, name='detalle_producto'),
]
