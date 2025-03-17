from django.contrib.auth.models import User
from django.utils import timezone
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.http import JsonResponse
from .models import PasswordReset
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
            if user.is_staff: 
                return JsonResponse({
                    'mensaje': f'Bienvenido {username}',
                    'is_admin': user.is_staff
                    }, status=200)
            elif user.groups.filter(name="vendedor").exists():
                return JsonResponse({
                    "mensaje": f"rol como vendedor señor@: {username}",
                    "rol": 'vendedor'
                }, status=200)
            elif user.groups.filter(name="logistica").exists():
                return JsonResponse({
                    "mensaje": f"rol como logistica señor@: {username}",
                    "rol": 'logistica'
                }, status=200)
            else:
                return JsonResponse({
                    "mensaje": f"Bienvenido {username}",
                })
        else:
            return JsonResponse({'error': 'Ups!, verifique sus credenciales...'}, status=400)
        
    
    return JsonResponse({'error':'Hubo un error.. intenta mas tarde :('})

@csrf_exempt
def logout(request):
    logout(request)
    return redirect ("http://localhost:5173/formAuth")

@csrf_exempt
def Solicitar_recuperacion(request):
    if request.method == 'POST': 
        data = json.loads(request.body)
        email = data.get('email')
        if not email:
            return JsonResponse({'error': 'El correo es obligatorio'}, status=404)
        
        try: 
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return JsonResponse({'error': 'Usuario no encontrado. Verifique'}, status=404)
        
        token = get_random_string(length=32)
        PasswordReset.objects.create(user=user, token=token, creado_en=timezone.now())

        send_mail(
            'Recuperación de contraseña',
            f'Utiliza este enlace para restablecer tu contraseña: http://localhost:5173/reset-password/{token}/',
            'noreply@example.com',
            [email],
        )

        return JsonResponse({'mensaje': 'Se a enviado un correo con instrucciones'}, status=200)
    
@csrf_exempt
def restablecer_contraseña(request, token):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_password = data.get('nueva_contraseña')
        if not new_password:
            return JsonResponse({'error': 'La contraseña es obligatoria'}, status=400)
        
        try: 
            reset_token = PasswordReset.objects.get(token=token)
        except PasswordReset.DoesNotExist:
            return JsonResponse({'error': 'este enlace ya no es valido o expiro'}, status=400)
        
        if (timezone.now() - reset_token.creado_en).days > 1:
            reset_token.delete()
            return JsonResponse({'error': 'Enlace expirado'}, status=400)
        
        user = reset_token.user
        user.set_password(new_password)
        user.save()

        reset_token.delete()

        return JsonResponse({'mensaje': 'La contraseña se restablecio exitosamente'}, status=200)