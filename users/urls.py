from django.urls import path
from .views import registro, ingreso,logout

urlpatterns = [
    path('registro/', registro, name='registroAPI'),
    path('ingreso/', ingreso, name='ingreso'),
    path('logout/', logout, name='logout'),
]