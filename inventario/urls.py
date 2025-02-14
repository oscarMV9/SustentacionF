from django.urls import path
from .  import views

urlpatterns = [
    path('catalogo/<str:prenda>', views.Catalogo_por_categoria,name='catalogo_por_categoria'),
    path('api/productos/<str:categoria>/', views.api_productos_por_categoria, name='api_productos_por_categoria'),
]