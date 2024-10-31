from rest_framework import viewsets
from .models import *
from .serializers import *

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    
class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer

class ComedorSolidarioViewSet(viewsets.ModelViewSet):
    queryset = ComedorSolidario.objects.all()
    serializer_class = ComedorSolidarioSerializer
    
class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    
class SectorViewSet(viewsets.ModelViewSet):
    queryset = Sector.objects.all()
    serializer_class = SectorSerializer
    
class RutaViewSet(viewsets.ModelViewSet):
    queryset = Ruta.objects.all()
    serializer_class = RutaSerializer
    
class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    
""" class Producto_PedidoViewSet(viewsets.ModelViewSet):
    queryset = Producto_Pedido.objects.all()
    serializer_class = Producto_PedidoSerializer """
    
""" class Rutas_ComedoresViewSet(viewsets.ModelViewSet):
    queryset = Rutas_Comedores.objects.all()
    serializer_class = Rutas_Comedores """

class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer

