from django.shortcuts import render, redirect
from .models import Appointments

# Create your views here.

def add_appointments(request):
    if request.method == 'POST':
        patient_name = request.POST['patient_name']
        doctors_name =  request.POST['doctor_name']
        time_slot = request.POST['time']
        department = request.POST['department']
        appointment_date = request.POST['date']
        token_number =  request.POST['number']
        problem =  request.POST['problem']
        appointment = Appointments.objects.create(
            patient_name=patient_name,
            doctor_name=doctors_name,
            time_slot=time_slot,
            department=department,
            appointment_date=appointment_date,
            token_number=token_number,
            problem=problem
        )
        appointment.save()
        return redirect('appointments:add_appointments')

    return render(request, 'appointments/add_appointments.html')

def appointments_list(request):
    appointment = Appointments.objects.all()
    context = {'appointments':appointment}
    return render(request, 'appointments/appointments_list.html', context)