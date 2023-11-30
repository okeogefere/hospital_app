from django.urls import path
from . import views

app_name = 'doctors'

urlpatterns = [
    path('add_doctors/', views.add_doctors, name='add_doctors'),
    path('doctors_list/', views.doctors_list, name='doctors_list'),
]