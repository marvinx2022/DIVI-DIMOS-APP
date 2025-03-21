from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView


def inicio(request):

    return render(request, "dividimos_app/inicio.html")



def login(request):

    return render(request, "dividimos_app/login.html")


# Vista para creación de nuevos usuarios:

class CrearUsuario(CreateView):
    form_class = UserCreationForm  
    template_name = "registration/registro.html"  
    success_url = reverse_lazy('inicio')  