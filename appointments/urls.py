from django.urls import path
from . import views

app_name = 'appointments'

urlpatterns = [
    path('add_appointments/', views.add_appointments, name='add_appointments'),
    path('appointments_list/', views.appointments_list, name='appointments_list'),
]