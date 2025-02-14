from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
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

        if User.objects.filter(username=username).exists():
            return JsonResponse({'error': 'Lo siento el usuario ya existe!'}, status=400)

        user = User.objects.create_user(username=username, email=email, password=password)
        return JsonResponse({'mensaje':'Usuario creado, bienvenido!'},status=201)

@csrf_exempt
def ingreso(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return JsonResponse({'mensaje': f'Bienvenido {username}'}, status=200)
        else:
            return JsonResponse({'error': 'Ups!, verifique sus credenciales...'}, status=400)
    
    return JsonResponse({'error':'El metodo no funciona o algo mas!, intenta de nuevc'})

