from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def registro(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        if User.objects.filter(email=email).exists():
            return JsonResponse({'error': 'este correo ya esta registrado'}, status=400)

        user = User.objects.create_user(username=username, email=email, password=password)
        return JsonResponse({'mensaje':'Usuario creado, bienvenido!'},status=201)

@csrf_exempt
def ingreso(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')

        try:
            user = User.objects.get(email=email)
            username = user.username
        except User.DoesNotExist:
            return JsonResponse({'error': 'Ups!, verifique sus credenciales...'}, status=400)
        
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return JsonResponse({
                'mensaje': f'Bienvenido {username}',
                'is_admin': user.is_staff
                }, status=200)
        else:
            return JsonResponse({'error': 'Ups!, verifique sus credenciales...'}, status=400)
    
    return JsonResponse({'error':'El metodo no funciona o algo mas!, intenta de nuevo'})

@csrf_exempt
def logout(request):
    logout(request)
    return redirect ("http://localhost:5173/formAuth")