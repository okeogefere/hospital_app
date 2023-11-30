from django.urls import path
from . import views

app_name = 'patients'

urlpatterns = [
    path('add_patients/', views.add_patients, name='add_patients'),
    path('about_patients/', views.about_patients, name='about_patients'),
    path('patients_list/', views.patients_list, name='patients_list'),
    path('edit_patients/', views.edit_patients, name='edit_patients'),
]