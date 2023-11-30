from django.shortcuts import render,redirect, get_object_or_404
from .models import Add_patients
from django.contrib import messages 

# Create your views here.

def add_patients(request):
    if request.method == 'POST':
        name = request.POST['name']
        date_of_birth = request.POST['date_of_birth']
        age = request.POST['age']
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        gender = request.POST['gender']
        address = request.POST['address']
        image = request.POST['image']
        add = Add_patients.objects.create(
            name=name,
            date_of_birth=date_of_birth,
            age=age,
            phone_number=phone_number,
            email=email,
            gender=gender,
            address=address,
    
        )
        add.save()
        messages.success(request, 'Patient added successfully!!')
        return redirect('patients:add_patients')

    return render(request, 'patients/add_patients.html')

def about_patients(request):
    return render(request, 'patients/about_patients.html')

def patients_list(request):
    patients = Add_patients.objects.all()
    context = {'patients':patients}
    return render(request, 'patients/patients_list.html', context)

def edit_patients(request):
    return render(request, 'patients/edit_patients.html')