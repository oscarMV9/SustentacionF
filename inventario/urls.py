from django.urls import path
from .views import categoriaProductos,productosGenero

urlpatterns = [
    path('productos/<str:categoria>/',categoriaProductos,name="categoriasProductos"),
    path('productos/genero/<str:categoria>/',productosGenero,name="productosGenero"),
]
