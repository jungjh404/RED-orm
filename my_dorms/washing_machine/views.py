import pytz
from django.shortcuts import render, get_object_or_404, redirect
from .models import Washing_Machine, Usage_Status, Reservation
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='common:login')
def status(request):
    status_lst = []
    if request.user.is_authenticated:
        machine_lst = Washing_Machine.objects.filter(building=request.user.building)
        for machine in machine_lst:
            status_dict = {
                'machine_id': machine
            }
            recent_use = machine.usage.order_by('-end_time').first()
            if recent_use is not None:
                status_dict['start_time'] = recent_use.start_time.timestamp()
                status_dict['end_time'] = recent_use.end_time.timestamp()
            status_lst.append(status_dict)
    
    status_form = {
        "building": request.user.building,
        "status_lst": status_lst
    }

    return render(request, 'washing_machine/status.html', status_form)

@login_required(login_url='common:login')
def add(request):
    if(request.method == 'POST'):
        pass

@login_required(login_url='common:login')
def camera(request):
    return render(request, 'washing_machine/camera.html')