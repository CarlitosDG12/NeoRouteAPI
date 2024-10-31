from django.contrib.auth.models import AbstractUser
from django.db import models

class Rol(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.nombre
    
class Usuario(AbstractUser):
    rut = models.CharField(max_length=12, unique= True)
    rol = models.ForeignKey(Rol, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
class EncargadoComedor(models.Model):
    rut = models.CharField(max_length=12, unique=True)
    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100, null=True)
    correo_electronico = models.CharField(max_length=100, unique= True)
    num_telefono = models.CharField(max_length=12)
    
    def __str__(self):
        return self.nombre + ' ' + self.apellido_paterno

class Sector(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre
    
class ComedorSolidario(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    latitud = models.DecimalField(max_digits=20, decimal_places=16)
    longitud = models.DecimalField(max_digits=20, decimal_places=16)
    encargado = models.ForeignKey(EncargadoComedor, on_delete=models.SET_NULL, null=True)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
        
class Ruta(models.Model):
    ruta = models.JSONField(null=True)
    dia_despacho = models.DateField() #Día planificado de despacho
    estado_ruta = models.CharField(max_length=50)#En proceso, Completada, Pendiente
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    conductor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
class Pedido(models.Model):
    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_entrega = models.DateField()
    hora_finalizacion = models.TimeField(null=True)
    estado = models.CharField(max_length=50)
    coordinador = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    comedor = models.ForeignKey(ComedorSolidario, on_delete=models.CASCADE)
    ruta_id = models.ForeignKey(Ruta, on_delete=models.CASCADE)
    
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    codigo_barras = models.CharField(max_length=255)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
    
class ProductoPedido(models.Model):
    cantidad = models.IntegerField()
    pedido = models.ForeignKey(Pedido, related_name='productos', on_delete= models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete= models.CASCADE)
    
class RutasComedores(models.Model):
    ruta = models.ForeignKey(Ruta, on_delete= models.CASCADE)
    comedor = models.ForeignKey(ComedorSolidario, on_delete= models.CASCADE)
    
class Vehiculo(models.Model):
    tipo = models.CharField(max_length=255)
    patente = models.CharField(max_length=20)
    conductor = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.tipo + ' ' + self.patente
    
