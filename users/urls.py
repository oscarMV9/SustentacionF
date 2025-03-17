from django.urls import path
from .views import registro, ingreso,logout, Solicitar_recuperacion, restablecer_contraseña

urlpatterns = [
    path('registro/', registro, name='registroAPI'),
    path('ingreso/', ingreso, name='ingreso'),
    path('logout/', logout, name='logout'),
    path('solicitar-recuperacion/', Solicitar_recuperacion, name='solicitar_recuperacion'),
    path('restablecer-contraseña/<str:token>/', restablecer_contraseña, name='restablecer-password'),
]