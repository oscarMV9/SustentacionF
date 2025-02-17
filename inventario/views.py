from django.shortcuts import render
from django.http import JsonResponse
from .models import Inventario

def categoriaProductos(request, categoria):
    productos = Inventario.objects.filter(categoriaPrenda__nombreCategoria__iexact=categoria)

    print(f"Productos encontrados para {categoria}: {productos}")

    if not productos:
        return JsonResponse({'error': 'No se encontraron productos para esta categoría'}, status=404)

    productos_json = [
        {
            'id': producto.idProducto.id,
            'nombre': producto.idProducto.get_nombre_producto(),
            'descripcion': producto.descripcion,
            'imagen': producto.idProducto.imagen.url if producto.idProducto.imagen else None,
            'precio': float(producto.idProducto.precio),
            'talla':str(producto.categoriaTalla.talla) if producto.categoriaTalla else None,
            'color':str(producto.categoriaColor.color) if producto.categoriaColor else None,
            'cantidad': producto.cantidades,
            'categoria_prenda': producto.categoriaPrenda.nombreCategoria
        }
        for producto in productos
    ]

    return JsonResponse({'categoria': categoria, 'productos': productos_json})

