from django.contrib import admin
import os
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from .views import index,home,catalogo,registro,ingreso,indexx
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', indexx, name='indexx'),
    path('registro/',TemplateView.as_view(template_name="templatesAuth/registro.html")),
    path('ingreso/',TemplateView.as_view(template_name="templatesAuth/login.html")),
    path('dashboard/',TemplateView.as_view(template_name="homeTemplates/home.html")),
    path('catalogo/', catalogo,name='catalogo'),
    path('api/usuarios/', include('users.urls')),
    path('invetario/', include('inventario.urls')),
    path('produccion/', include('produccion.urls')),
    path('ventas/', include('ventas.urls')),
] + static(settings.STATIC_URL, document_root=os.path.join(settings.BASE_DIR, 'frontEnd', 'dist', 'assets'))
