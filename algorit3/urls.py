from django.urls import path
from . import views

urlpatterns = [

    path('algorit3/', views.regresionLog, name='algorit3'),

]