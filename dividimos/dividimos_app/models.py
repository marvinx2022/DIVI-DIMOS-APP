from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator



class Usuario(AbstractUser):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(
        max_length=15, 
        blank=True, 
        null=True, 
        validators=[
            RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Ingrese un número de teléfono válido.")
        ]
    )
    email = models.EmailField(unique=True, blank=True, null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['nombre', 'apellido']
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"




#Evento


#Invitado


