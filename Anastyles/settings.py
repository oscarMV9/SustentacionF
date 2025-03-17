
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-uonw+^rqz!02q!%_if=d%9*wupboi*x!i0st7wr5=3l+__7g6z'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',
    'jazzmin',
    'import_export',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'inventario',
    'produccion',
    'ventas',
    'Categorias',
    'logistica',
    'carrito',
    'users',
]

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": "navbar-success",
    "accent": "accent-teal",
    "navbar": "navbar-dark",
    "no_navbar_border": False,
    "navbar_fixed": True,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": True,
    "sidebar": "sidebar-dark-olive",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": True,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": True,
    "theme": "darkly",
    "dark_mode_theme": "darkly",
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-outline-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    },
    "actions_sticky_top": False
}

JAZZMIN_SETTINGS = {
    "site_title": "AnaStyles",
    "site_header": "AnaStyles",
    "site_brand": "Admin AnaStyles",
    "show_ui_builder": True,
    # "site_logo": "/staticfiles/imagenes/AnaStyle.png",
    "theme": "darkly",
    "navigation_expanded": False,
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "auth_users.Profile": "fas fa-user",
        "auth_users": "fas fa-users-cog",
        "inventario":"fas fa-clipboard-list",
        "inventario.purchase_of_inputs":"fa-solid fa-truck-fast",
        "inventario.product":"fa-solid fa-bag-shopping",
        "inventario.brand":"fa-solid fa-tag",
        "inventario.supplier":"fa-solid fa-truck-field-un",
        "inventario.category":"fa-solid fa-list",
        "ventas":"fas fa-shopping-cart",
        "ventas.Venta":"fas fa-shopping-cart",
        "ventas.Venta_DetalleVenta":"fas fa-shopping-cart",
    },
    "copyright": "AnaStyles 2025",
    "topmenu_links": [
        # Ícono de campana para notificaciones
        {
            "name": "Notificaciones",
            "url": "",  # Ruta a la vista de notificaciones
            "icon": "fas fa-bell",  # Ícono de FontAwesome
            "permissions": ["auth.view_user"],  # Permisos requeridos
        },
        ],
         "custom_css": "admin_styles.css",  # Cargar CSS personalizado
    # "welcome_sign": "Bienvenido al panel de admin :)))",
    # "theme": "dark",
    # "site_title": "Admin Biblioteca",
    # "site_header": "Sistema de Administración de la Biblioteca",
}

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:8000",
    "http://localhost:8000",
    "https://9vtnjg7h-5173.use2.devtunnels.ms",  
    "https://9vtnjg7h-8000.use2.devtunnels.ms",

]

CORS_ALLOW_ALL_ORIGINS = True 
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_METHODS = ["GET", "POST", "PUT", "DELETE", "OPTIONS"]
CORS_ALLOW_HEADERS = ["*"]

ALLOWED_HOSTS = [
    "9vtnjg7h-5173.use2.devtunnels.ms",
    "9vtnjg7h-8000.use2.devtunnels.ms",  
    "localhost",
    "127.0.0.1",
]

ROOT_URLCONF = 'Anastyles.urls'

import os

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'frontEnd', 'dist')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # Servidor SMTP de Gmail
EMAIL_PORT = 587  # Puerto SMTP
EMAIL_USE_TLS = True  # Seguridad TLS
EMAIL_HOST_USER = 'anastylesgaes4@gmail.com'
EMAIL_HOST_PASSWORD = 'qophzimkjkawiljv'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
#DEFAULT_FROM_EMAIL = 'tu_correo@gmail.com'  # Dirección de correo predeterminada para el envío
#qoph zimk jkaw iljv

WSGI_APPLICATION = 'Anastyles.wsgi.application'

from . import db as db

DATABASES = db.MYSQL


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'http://localhost:5173/formAuth'


LANGUAGE_CODE = 'es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
