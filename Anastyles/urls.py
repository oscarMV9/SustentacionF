from django.contrib import admin
import os
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('inventario.urls')),
    path('api/usuarios/', include('users.urls')),
    path('productos/<str:categoria>/', TemplateView.as_view(template_name='homeTemplates/productos.html'), name='productos'),
    path('ventas/', include('ventas.urls')),
] + static(settings.STATIC_URL, document_root=os.path.join(settings.BASE_DIR, 'frontEnd', 'dist', 'assets'))
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
