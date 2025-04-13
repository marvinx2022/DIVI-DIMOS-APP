from django.urls import path
from dividimos_app.views import inicio, CrearUsuario, crear_evento, agregar_invitados, resumen_aportes, resultado
from django.contrib.auth import views as auth_views


urlpatterns = [
    
    path('inicio', inicio, name='inicio'),
    path('login', auth_views.LoginView.as_view(), name='login'),
    path("registro/", CrearUsuario.as_view(), name="registro"),
    path("crear_evento/", crear_evento, name="evento"),
    path("agregar_invitados/", agregar_invitados, name="invitados"),
    path("resumen_aportes/", resumen_aportes, name="resumen"),
    path("resultado/", resultado, name="resultado")
   
]
