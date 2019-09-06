from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=250)
    codigo = models.CharField(max_length=15, unique=True, null=True)
    precio = models.DecimalField(max_digits=7, decimal_places=2, validators=[MinValueValidator(0)])
    #precio.clean(0)
    def __str__(self):
        return self.nombre
