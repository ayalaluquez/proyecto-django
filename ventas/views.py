from django.shortcuts import render
from rest_framework import viewsets
from .models import Producto
from .serializers import ProductoModelSerializer


# Create your views here.
class ProductoViewSet(viewsets.ModelViewSet):

    queryset = Producto.objects.all()
    serializer_class = ProductoModelSerializer


# Create your views here.
