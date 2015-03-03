from django.shortcuts import render
#from django.shortcuts import render_to_response
#from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
#from django.core.context_processors import csrf
#from django.shortcuts import render, get_objects_or_404
from django.shortcuts import redirect
from django.utils import timezone
from .models import Appointment


def appointment_list(request):
    appointments = Appointment.objects.filter(appointment_date__lte=timezone.now()).order_by('appointment_date')
    return render(request, 'clinic/appointment_list.html', {'appointments':appointments})

def prescription_list(request):

    return render(request, 'clinic/prescription_list.html', {})


