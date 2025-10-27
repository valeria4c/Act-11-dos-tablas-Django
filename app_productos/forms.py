from django import forms
from .models import Categorias, Productos

# ===========================
# FORMULARIO CATEGORÍAS
# ===========================
class CategoriaForm(forms.ModelForm):
    # Campo solo lectura para fecha de creación
    fecha_creacion = forms.DateTimeField(
        label="Fecha de creación",
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control',
            'type': 'datetime-local',
            'readonly': 'readonly'
        }),
        required=False
    )

    # Campo solo lectura para id_categoria
    id_categoria = forms.IntegerField(
        label="ID Categoría",
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'readonly': 'readonly'
        }),
        required=False
    )

    class Meta:
        model = Categorias
        # Solo campos editables aquí
        fields = ['nombre', 'descripcion', 'activa']  
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'activa': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

# ===========================
# FORMULARIO PRODUCTOS
# ===========================
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ['id_producto','nombre', 'descripcion', 'precio', 'stock', 'id_categoria', 'imagen_url', 'id_detalle_de_producto']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'id_categoria': forms.Select(attrs={'class': 'form-control'}),  # 🔹 select de categorías
            'imagen_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Pega aquí la URL de la imagen'}),
            'id_detalle_de_producto': forms.NumberInput(attrs={'class': 'form-control'}),
        }
