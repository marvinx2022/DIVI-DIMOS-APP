from django.shortcuts import render

def index(request):

    return render(request, "dividimos_app/index.html")