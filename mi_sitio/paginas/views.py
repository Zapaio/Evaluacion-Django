from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def inicio(request):
    return render(request,"paginas\inicio.html")

def contacto(request):
    return render(request,"paginas\contacto.html")

def acerca(request):
    return render(request,r"C:\INFOR1\Evaluacion1\mi_sitio\paginas\templates\paginas\acerca.html")