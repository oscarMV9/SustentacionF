from django.shortcuts import render
from django.http import JsonResponse
from django.urls import reverse_lazy
from .models import Productos, Inventario

def Catalogo_por_categoria(request, prenda):
    productos = Inventario.objects.filter(categoriaPrenda__nombreCategoria=prenda)
    return render(request, 'productos.html', {'productos':productos, 'filtro': f'Prenda: {prenda}'})


def api_productos_por_categoria(request, categoria):
    productos = Inventario.objects.filter(categoriaPrenda__nombreCategoria=categoria)

    productos_json = [
        {
            'id': producto.idProducto.id,
            'nombre': producto.idProducto.get_nombre_producto(),
            'descripcion': producto.descripcion,
            'precio': str(producto.idProducto.precio), 
            'cantidad': producto.cantidades,
            'categoria_prenda': producto.categoriaPrenda.nombreCategoria 
        }
        for producto in productos
    ]

    return JsonResponse({'categoria': categoria, 'productos': productos_json})

