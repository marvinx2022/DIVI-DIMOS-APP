from django.db import models
from django.contrib.auth.models import User

class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()
    lugar = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nombre} - {self.fecha}"


class Invitado(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='invitados')
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    usuario_asociado = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    email = models.EmailField(blank=True, null=True)
    celular = models.CharField(max_length=20, blank=True, null=True)
    agasajado = models.BooleanField(default=False)  # No aporta si es True

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Aporte(models.Model):
    TIPO_APORTE = (
        ('dinero', 'Dinero'),
        ('mercancia', 'Mercancía'),
    )
    invitado = models.ForeignKey(Invitado, on_delete=models.CASCADE, related_name='aportes')
    tipo = models.CharField(max_length=10, choices=TIPO_APORTE)
    descripcion = models.CharField(max_length=200, blank=True)
    valor_estimado = models.DecimalField(max_digits=10, decimal_places=2)  # usado para ambos tipos

    def __str__(self):
        return f"{self.tipo.capitalize()} - {self.valor_estimado} ({self.invitado})"


class Resultado(models.Model):
    evento = models.OneToOneField(Evento, on_delete=models.CASCADE, related_name='resultado')
    total_recaudado = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_gastos = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    aportes_individuales = models.JSONField(default=dict)  # {"invitado_id": valor_aporte}
    division_gastos = models.JSONField(default=dict)       # {"invitado_id": cuanto_deberia_aportar}

    def __str__(self):
        return f"Resultados de {self.evento.nombre}"
