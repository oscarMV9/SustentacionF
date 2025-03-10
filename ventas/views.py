from rest_framework import viewsets
from .models import Venta,VentaItem
from .serializers import VentaItemSerializer, VentaSerializer

class VistaVentas(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer

class VistaVentaItem(viewsets.ModelViewSet):
    queryset = VentaItem.objects.all()
    serializer_class = VentaItemSerializer