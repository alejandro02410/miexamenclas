from django.urls import path
from . import views

urlpatterns = [

    path('algorit3/', views.muestra_datos, name='algorit3'),

]