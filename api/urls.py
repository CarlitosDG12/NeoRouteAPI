from django.urls import path,include
from rest_framework import routers
from api import views

router=routers.DefaultRouter()
router.register(r'roles', views.RolViewSet)
router.register(r'usuarios', views.UsuarioViewSet)
router.register(r'sectores', views.SectorViewSet)
router.register(r'comedores', views.ComedorSolidarioViewSet)
router.register(r'categorias', views.CategoriaViewSet)
router.register(r'productos', views.ProductoViewSet)
router.register(r'rutas', views.RutaViewSet)
router.register(r'pedidos', views.PedidoViewSet)
router.register(r'vehiculos', views.VehiculoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]