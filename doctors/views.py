from django.shortcuts import render

# Create your views here.

def add_doctors(request):
    return render(request, 'doctors/add_doctors.html')

def doctors_list(request):
    return render(request, 'doctors/doctors_list.html')