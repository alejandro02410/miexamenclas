from django.urls import path
from . import views

urlpatterns = [

    path('inicio/', views.muestra_datos, name='inicio'),

]