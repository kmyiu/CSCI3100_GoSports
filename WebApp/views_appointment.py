from django.db.models import Field
from django.shortcuts import render, redirect, get_object_or_404
from .models import Appointment
from django.http import HttpResponse
from .forms import AppointmentForm
from django.utils import timezone

# Print all fields in appointment except participants
header = [f.name for f in Appointment._meta.get_fields() if f.name!='participants']

# This view handles the appointment list
def appointment_list(request):
    all_obj = Appointment.objects.all().order_by('id')
    lst = []
    present = timezone.now()
    for obj in all_obj:
        # To update status of appointment
        if not (present < getattr(obj, 'appointment_time')):
            obj.status = 'E'
        elif obj.max_num == obj.joined:
            obj.status = 'F'
        obj.save()
        allowed = (obj.status == 'O') and (request.user.id not in eval(obj.participants)) and \
         (request.user.id != obj.starter.id) 
        lst.append([getattr(obj, 'id'), [(t,getattr(obj, t)) for t in header], allowed])
    return render(request, 'WebApp/appointment_list.html', {'appointments': lst})

# This view handles joining appointments
def appointment_join(request, pk):
    appointment = get_object_or_404(Appointment, pk = pk)
    lst = []
    if appointment:
        lst = tuple([(t,getattr(appointment, t)) for t in header])
    return render(request, 'WebApp/appointment_join.html', {'appointment': lst, 'id': pk})

# This view handles creating new appointments
def appointment_new(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        errors = []
        if form.is_valid():
            instance = form.save(commit=False)
            instance.starter = request.user
            instance.save()
        else:
            for error_key in form.errors.keys():
                errors.append(form.errors[error_key])
        request.session['errors'] = errors
        return redirect('appointment_list')
    else:
        form = AppointmentForm(request.POST)
    return render(request, 'WebApp/appointment_new.html', {'form': form})

# This view handles the joining results of appointments
def appointment_join_result(request, pk):
    lst = []
    appointment = get_object_or_404(Appointment, pk = pk)
    if appointment:
        new_participants = eval(appointment.participants)
        new_participants.append(request.user.id)
        new_participants = str(new_participants)
        new_joined = appointment.joined + 1
        setattr(appointment, 'participants', new_participants)
        setattr(appointment, 'joined', new_joined)
        present = timezone.now()
        if not (present < getattr(appointment, 'appointment_time')):
            appointment.status = 'E'
        elif appointment.max_num == appointment.joined:
            appointment.status = 'F'
        appointment.save()
        lst = tuple([(t,getattr(appointment, t)) for t in header])
    return render(request, 'WebApp/appointment_join_result.html', {'appointment': lst})