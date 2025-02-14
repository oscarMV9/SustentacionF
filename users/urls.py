from django.urls import path
from .views import registro, ingreso
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('registro/', registro, name='registro'),
    path('ingreso/', ingreso, name='ingreso'),
]