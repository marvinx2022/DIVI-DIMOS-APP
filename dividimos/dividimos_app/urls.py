from django.contrib import admin
from django.urls import path
from dividimos_app.views import index


urlpatterns = [
    path('inicio', index)
    
]
