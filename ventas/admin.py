from django.contrib import admin
from .models import Producto
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nombre', 'descripcion', 'precio']
    list_filter = ['codigo', 'nombre']
    search_fields = ['nombre']
    #prepopulated_fields = {'title': ('title',)}

admin.site.register(Producto, ProductoAdmin)
