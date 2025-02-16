from django.urls import path
from .views import registro, ingreso

urlpatterns = [
    path('registro/', registro, name='registroAPI'),
    path('ingreso/', ingreso, name='ingreso'),
]