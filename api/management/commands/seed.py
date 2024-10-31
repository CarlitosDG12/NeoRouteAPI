import random
from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker
from api.models import Rol, Usuario, Sector, ComedorSolidario, Categoria, Producto, Ruta, Pedido, ProductoPedido, Vehiculo

fake = Faker()

class Command(BaseCommand):
    help = 'Seed data for testing purposes'

    def handle(self, *args, **kwargs):
        self.clear_data()
        self.create_roles()
        self.create_users()
        self.create_sectors()
        self.create_comedores()
        self.create_categorias()
        self.create_productos()
        self.create_rutas()
        self.create_pedidos()
        print("Database seeded successfully.")

    def clear_data(self):
        # Elimina datos anteriores para evitar duplicados
        ProductoPedido.objects.all().delete()
        Pedido.objects.all().delete()
        Ruta.objects.all().delete()
        Vehiculo.objects.all().delete()
        Producto.objects.all().delete()
        Categoria.objects.all().delete()
        ComedorSolidario.objects.all().delete()
        Sector.objects.all().delete()
        Usuario.objects.all().delete()
        Rol.objects.all().delete()
    
    def create_roles(self):
        roles = ["Conductor", "Coordinador"]
        for rol in roles:
            Rol.objects.create(nombre=rol)
    
    def create_users(self):
        for _ in range(10):  # Crea 10 usuarios de prueba
            role = Rol.objects.order_by('?').first()
            Usuario.objects.create(
                username=fake.user_name(),
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.email(),
                password="password123",  # En producción usa make_password
                rut=fake.unique.ean13(),
                rol=role
            )

    def create_sectors(self):
        for _ in range(5):  # Crea 5 sectores
            Sector.objects.create(nombre=fake.city())
    
    def create_comedores(self):
        for _ in range(10):  # Crea 10 comedores solidarios
            ComedorSolidario.objects.create(
                nombre=fake.company(),
                direccion=fake.address(),
                latitud=fake.latitude(),
                longitud=fake.longitude(),
                encargado=Usuario.objects.filter(rol__nombre="Encargado").order_by('?').first(),
                sector=Sector.objects.order_by('?').first()
            )
    
    def create_categorias(self):
        for _ in range(5):  # Crea 5 categorías
            Categoria.objects.create(nombre=fake.word().capitalize())

    def create_productos(self):
        for _ in range(20):  # Crea 20 productos
            Producto.objects.create(
                nombre=fake.word().capitalize(),
                descripcion=fake.sentence(),
                codigo_barras=fake.unique.ean13(),
                categoria=Categoria.objects.order_by('?').first()
            )
    
    def create_rutas(self):
        for _ in range(10):  # Crea 10 rutas
            Ruta.objects.create(
                dia_despacho=timezone.now().date(),
                estado_ruta=random.choice(['En proceso', 'Completada', 'Pendiente']),
                sector=Sector.objects.order_by('?').first(),
                conductor=Usuario.objects.filter(rol__nombre="Conductor").order_by('?').first()
            )
    
    def create_pedidos(self):
        for _ in range(10):  # Crea 10 pedidos con productos asociados
            pedido = Pedido.objects.create(
                fecha_entrega=timezone.now().date(),
                estado=random.choice(['Pendiente', 'Entregado', 'Cancelado']),
                coordinador=Usuario.objects.filter(rol__nombre="Coordinador").order_by('?').first(),
                comedor=ComedorSolidario.objects.order_by('?').first(),
                ruta_id=Ruta.objects.order_by('?').first()
            )
            for _ in range(3):  # Cada pedido tiene 3 productos
                ProductoPedido.objects.create(
                    cantidad=random.randint(1, 10),
                    pedido=pedido,
                    producto=Producto.objects.order_by('?').first()
                )

