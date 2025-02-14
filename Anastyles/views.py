from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

# vista de registro y login
@api_view(['POST'])
def registro(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if User.objects.filter(username=username).exists():
        return Response({'error': 'Usuario ya existe'}, status=status.HTTP_400_BAD_REQUEST)
    
    user = User.objects.create_user(username=username, password=password)
    return Response({'mensaje': 'Usuario creado'}, status=status.HTTP_201_CREATED)

def ingreso(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)
    if user:
        return Response({'mensaje': 'Bienvenido!'}, status=status.HTTP_200_OK)
    return Response({'error': 'Usuario o contraseña incorrectos'}, status=status.HTTP_400_BAD_REQUEST)
    
def indexx(request):
    return render(request, "index.html")

# aqui esta el registro
def registro(request):
    return render(request, "templatesAuth/registro.html")

def index(request):
    return render(request, 'index.html')

def catalogo(request):
    return render(request, 'catalogo.html')

@login_required
def home(request):
    return render(request, 'home.html')
