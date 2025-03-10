from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"ventas", views.VistaVentas, 'ventas')
router.register(r"ventaItems",views.VistaVentaItem, 'ventaItem')

urlpatterns = [
    path("ventas/", include(router.urls))
]