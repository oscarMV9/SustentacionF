from django.urls import path
from .views import registro, ingreso,logout, Solicitar_recuperacion

urlpatterns = [
    path('registro/', registro, name='registroAPI'),
    path('ingreso/', ingreso, name='ingreso'),
    path('logout/', logout, name='logout'),
    path('solicitar-recuperacion/', Solicitar_recuperacion, name='solicitar_recuperacion'),
]