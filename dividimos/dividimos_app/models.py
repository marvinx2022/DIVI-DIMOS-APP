from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.core.validators import RegexValidator
from django.conf import settings




class Usuario(AbstractUser):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    pais = models.CharField(max_length=40)
    telefono = models.CharField(
        max_length=20, 
        blank=True, 
        null=True, 
    )
    email = models.EmailField(unique=True, blank=True, null=True)
    groups = models.ManyToManyField(Group, related_name="usuario_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="usuario_permissions", blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['nombre', 'apellido']
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Evento(models.Model):
    nombre = models.CharField(max_length=255)
    fecha = models.DateField()
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="eventos")

    def __str__(self):
        return self.nombre
    
    
    
# Modelo que relaciona el invitado con el evento, este campo la va a actualizar el usuario registrado que cree el evento. 

class Invitado(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name="invitados")
    nombre = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} ({self.evento.nombre})"


# Aporte relacionado con invitado y evento. 
class Aporte(models.Model):
    invitado = models.ForeignKey(Invitado, on_delete=models.CASCADE, related_name="aportes")
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name="aportes")
    dinero = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    mercaderia = models.TextField(blank=True, null=True)  
    precio_mercaderia = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Aporte de {self.invitado.nombre} para {self.evento.nombre}"
