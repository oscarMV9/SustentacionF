from django.db import models
from django.contrib.auth.models import User

class PasswordReset(models.Model): 
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    token = models.CharField(max_length=32,unique=True)
    creado_en = models.DateTimeField(auto_now_add=True)

# Create your models here.
