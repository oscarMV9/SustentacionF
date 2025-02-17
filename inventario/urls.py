from django.urls import path
from .views import categoriaProductos
from django.views.generic import TemplateView

urlpatterns = [
    path('productos/<str:categoria>/',categoriaProductos,name="categoriasProductos"),
]
