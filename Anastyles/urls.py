from django.contrib import admin
import os
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="indexesTemplates/index.html"), name='index'),
    path('registro/',TemplateView.as_view(template_name="templatesAuth/registro.html"), name='registroU'),
    path('ingreso/',TemplateView.as_view(template_name="templatesAuth/login.html"), name='login'),
    path('dashboard/',TemplateView.as_view(template_name="homeTemplates/home.html")),
    path('carrito/',TemplateView.as_view(template_name="homeTemplates/carrito.html")),
    path('api/',include('inventario.urls')),
    path('api/usuarios/', include('users.urls')),
    path('productos/<str:categoria>/', TemplateView.as_view(template_name='homeTemplates/productos.html'), name='productos'),
    path('inven tario/', include('inventario.urls')),
    path('produccion/', include('produccion.urls')),
    path('ventas/', include('ventas.urls')),
] + static(settings.STATIC_URL, document_root=os.path.join(settings.BASE_DIR, 'frontEnd', 'dist', 'assets'))
