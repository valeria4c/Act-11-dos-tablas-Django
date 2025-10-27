from django.db import models

from django.db import models

class Categorias(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    activa = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Productos(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=25)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    id_categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    imagen_url = models.URLField(max_length=500, blank=True, null=True)
    id_detalle_de_producto = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.nombre