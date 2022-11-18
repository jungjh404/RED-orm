import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import Washing_Machine, Usage_Status, Reservation
from .ocr import img_ocr


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
        current_time = timezone.now()
        img = request.POST["ocr-image"]
        pos = request.POST["ocr-position"]
        code = request.POST["code-data"]
        machine = Washing_Machine.objects.get(id=code)
        ocr_result = img_ocr(img)
        
        if ocr_result is not None:
            Usage_Status.objects.create(
                machine_id=machine,
                user_id=request.user,
                start_time=current_time,
                modified_time=current_time,
                end_time=current_time + datetime.timedelta(minutes=ocr_result)
            )
            return redirect('washing_machine:add')

    messages.warning(request, "다시 촬영해주세요.")
    return redirect('washing_machine:status')

@login_required(login_url='common:login')
def camera(request):
    return render(request, 'washing_machine/test_camera.html')