# ...existing code...
INSTALLED_APPS = [
    # ...existing code...
    'jazzmin',
    'corsheaders',
    'import_export',
    # ...existing code...
]

MIDDLEWARE = [
    # ...existing code...
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    # ...existing code...
]

# Configuración de CORS
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    # Agrega aquí los orígenes permitidos
]
# ...existing code...
