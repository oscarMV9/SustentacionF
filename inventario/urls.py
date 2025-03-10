from django.urls import path
from .views import categoriaProductos,productosGenero,productoID,productosTallas

urlpatterns = [
    path('productos/<str:categoria>/',categoriaProductos,name="categoriasProductos"),
    path('productos/genero/<str:categoria>/',productosGenero,name="productosGenero"),
    path('producto/<int:id>/', productoID,name="productosId"),
    path('productos/tallas/<str:categoria>',productosTallas,name="productosTallas")
]
