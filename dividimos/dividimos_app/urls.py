from django.urls import path
from dividimos_app.views import inicio, CrearUsuario
from django.contrib.auth import views as auth_views


urlpatterns = [
    
    path('inicio', inicio, name='inicio'),
    #path('login', login),
    path('login', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path("registro/", CrearUsuario.as_view(), name="registro")
    
]
