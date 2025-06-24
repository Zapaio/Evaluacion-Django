from django.urls import path
from . import views
from django.http import HttpResponse

urlpatterns=    [
                path("",views.inicio),
                path("contacto",views.contacto),
                path("acerca",views.acerca),]