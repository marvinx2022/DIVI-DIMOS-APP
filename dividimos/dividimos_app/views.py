from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView


def inicio(request):
    return render(request, "dividimos_app/inicio.html")

def login(request):
    return render(request, "dividimos_app/login.html")

def crear_evento(request):
    return render(request, "dividimos_app/crear_evento.html")

def agregar_invitados(request):
    return render(request, "dividimos_app/agregar_invitados.html")

def resumen_aportes(request):
    return render(request, "dividimos_app/resumen_aportes.html")

def resultado(request):
    return render(request, "dividimos_app/resultado.html")

def dashboard(request):
    return render(request, "dividimos_app/dashboard.html")

# Vista para creación de nuevos usuarios:

class CrearUsuario(CreateView):
    form_class = UserCreationForm  
    template_name = "registration/registro.html"  
    success_url = reverse_lazy('inicio')  