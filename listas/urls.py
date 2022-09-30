from django.urls import path
from . import views

urlpatterns = [

    path('listas/', views.muestra_datos, name='listas'),

]