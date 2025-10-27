from django.shortcuts import render, redirect, get_object_or_404
from .models import Categorias, Productos
from .forms import CategoriaForm, ProductoForm

# ===========================
# VISTAS CATEGORÍAS
# ===========================

def listar_categorias(request):
    categorias = Categorias.objects.all()
    return render(request, 'categorias/listar_categorias.html', {'categorias': categorias})

def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app_productos:listar_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'categorias/crear_categoria.html', {'form': form, 'titulo': 'Crear Categoría'})

def editar_categoria(request, id):
    categoria = get_object_or_404(Categorias, id_categoria=id)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('app_productos:listar_categorias')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'categorias/editar_categoria.html', {'form': form, 'titulo': 'Editar Categoría'})

def eliminar_categoria(request, id):
    categoria = get_object_or_404(Categorias, id_categoria=id)
    categoria.delete()
    return redirect('app_productos:listar_categorias')

def detalle_categoria(request, id):
    categoria = get_object_or_404(Categorias, id_categoria=id)
    productos = Productos.objects.filter(id_categoria=categoria)
    return render(request, 'categorias/detalle_categoria.html', {
        'categoria': categoria,
        'productos': productos
    })


# ===========================
# VISTAS PRODUCTOS
# ===========================

def listar_productos(request):
    productos = Productos.objects.all()
    return render(request, 'productos/listar_productos.html', {'productos': productos})

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app_productos:listar_productos')
    else:
        form = ProductoForm()
    return render(request, 'productos/crear_producto.html', {'form': form, 'titulo': 'Crear Producto'})

def editar_producto(request, id):
    producto = get_object_or_404(Productos, id_producto=id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('app_productos:listar_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'productos/editar_producto.html', {'form': form, 'titulo': 'Editar Producto'})

def eliminar_producto(request, id):
    producto = get_object_or_404(Productos, id_producto=id)
    producto.delete()
    return redirect('app_productos:listar_productos')


# ===========================
# VISTA DETALLE PRODUCTO
# ===========================

def detalle_producto(request, id):
    producto = get_object_or_404(Productos, id_producto=id)
    return render(request, 'productos/detalle_producto.html', {'producto': producto})
