from django.urls import path, include
from . import views


urlpatterns=    [
                path("",views.inicio,name="inicio"),
                path("contacto",views.contacto,name="contacto"),
                path("acerca",views.acerca,name="acerca"),]