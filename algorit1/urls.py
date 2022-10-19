from django.urls import path
from . import views

urlpatterns = [

    path('algorit1/', views.muestra_datos, name='algorit1'),

]