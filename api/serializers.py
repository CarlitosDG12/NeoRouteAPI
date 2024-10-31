from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id','rut','username','first_name','last_name','email','password','rol']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(UsuarioSerializer, self).create(validated_data)
    
class RolSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Rol
        fields = '__all__'

class ComedorSolidarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComedorSolidario
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
        
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'
        
class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = '__all__'
        
class RutaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ruta
        fields = '__all__'
        
class ProductoPedidoSerializer(serializers.ModelSerializer):
    nombre_producto = serializers.CharField(source='producto.nombre', read_only=True)
    producto = serializers.PrimaryKeyRelatedField(queryset=Producto.objects.all())

    class Meta:
        model = ProductoPedido
        fields = ['nombre_producto', 'cantidad', 'producto']

class PedidoSerializer(serializers.ModelSerializer):
    productos = ProductoPedidoSerializer(many=True)

    class Meta:
        model = Pedido
        fields = ['fecha_creacion', 'fecha_entrega', 'hora_finalizacion', 'estado', 'coordinador', 'comedor', 'ruta_id', 'productos']

    def create(self, validated_data):
        productos_data = validated_data.pop('productos')
        pedido = Pedido.objects.create(**validated_data)
        for producto_data in productos_data:
            producto = producto_data.pop('producto')
            ProductoPedido.objects.create(pedido=pedido, producto=producto, **producto_data)
        return pedido

    def update(self, instance, validated_data):
        productos_data = validated_data.pop('productos')
        instance.fecha_entrega = validated_data.get('fecha_entrega', instance.fecha_entrega)
        instance.hora_finalizacion = validated_data.get('hora_finalizacion', instance.hora_finalizacion)
        instance.estado = validated_data.get('estado', instance.estado)
        instance.coordinador = validated_data.get('coordinador', instance.coordinador)
        instance.comedor = validated_data.get('comedor', instance.comedor)
        instance.ruta_id = validated_data.get('ruta_id', instance.ruta_id)
        instance.save()

        # Actualizar productos
        instance.productos.all().delete()
        for producto_data in productos_data:
            producto = producto_data.pop('producto')
            ProductoPedido.objects.create(pedido=instance, producto=producto, **producto_data)

        return instance
    
class Rutas_ComedoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = RutasComedores
        fields = '__all__'
        
class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = '__all__'

