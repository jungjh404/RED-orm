import datetime
import json
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import Washing_Machine, Usage_Status, Reservation
from .ocr import img_ocr
from .webpush import machine_done_webpush

# Create your views here.
@login_required(login_url='common:login')
def status(request):
    status_lst = []
    if request.user.is_authenticated:
        if request.user.building is None:
            messages.warning(request, "회원정보를 업데이트해주세요.")
            return redirect('common:profile')
        machine_lst = Washing_Machine.objects.filter(building=request.user.building)
        for machine in machine_lst:
            status_dict = {
                'machine_id': machine
            }
            recent_use = machine.usage.filter(done=False).order_by('-end_time').first()
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
    current_time = timezone.now()
    img = request.POST["ocr-image"]
    pos = request.POST["ocr-position"]
    code = json.loads(request.POST["code-data"])["id"]

    try:
        machine = Washing_Machine.objects.get(id=code)
    except Washing_Machine.DoesNotExist:
        messages.warning(request, "잘못된 QR코드입니다.")
        return redirect('washing_machine:status')

    recent_use = Usage_Status.objects.filter(machine_id=machine, done=False)

    if len(recent_use) > 0:
        messages.warning(request, "이미 사용 중인 세탁기입니다.")
        return redirect('washing_machine:status')

    ocr_result = img_ocr(img)

    if ocr_result is not None:
        Usage_Status.objects.create(
            machine_id=machine,
            user_id=request.user,
            start_time=current_time,
            modified_time=current_time,
            end_time=current_time + datetime.timedelta(minutes=ocr_result),
            done=False
        )
        messages.warning(request, "등록이 완료되었습니다.")
        return redirect('washing_machine:status')

    messages.warning(request, "다시 촬영해주세요.")
    return redirect('washing_machine:status')


@login_required(login_url='common:login')
def reserve(request):
    if(request.method == 'POST'):
        current_time = timezone.now()
        img = request.POST["ocr-image"]
        pos = request.POST["ocr-position"]
        code = json.loads(request.POST["code-data"])["id"]
        try:
            machine = Washing_Machine.objects.get(id=code)
        except Washing_Machine.DoesNotExist:
            messages.warning(request, "잘못된 QR코드입니다.")
            return redirect('washing_machine:status')
        
        recent_use = Usage_Status.objects.filter(machine_id=machine, done=False)

        if len(recent_use) == 0:
            messages.warning(request, "사용 중이지 않은 세탁기입니다.")
            return redirect('washing_machine:status')
        
        reserve_check = Reservation.objects.filter(machine_id=machine, usage_id=recent_use[0])
        if len(reserve_check) > 0:
            messages.warning(request, "이미 예약하셨습니다.")
            return redirect('washing_machine:status')

        ocr_result = img_ocr(img)
        
        if ocr_result is not None:
            Reservation.objects.create(
                machine_id=machine,
                user_id=request.user,
                usage_id=recent_use[0],
                reservation_time=current_time,
                done=False
            )
            messages.warning(request, "등록이 완료되었습니다.")
            return redirect('washing_machine:status')

    messages.warning(request, "다시 촬영해주세요.")
    return redirect('washing_machine:status')


@login_required(login_url='common:login')
def camera(request):
    return render(request, 'washing_machine/test_camera.html')


@login_required(login_url='common:login')
def reserve_camera(request):
    return render(request, 'washing_machine/test_reserve.html')


def alarm_check():
    done_states = Usage_Status.objects.filter(end_time__lt=timezone.now(), done=False)
    
    if len(done_states) != 0:
        for state in done_states:
            state.done = True
            
            reserve_lst = Reservation.objects.filter(usage_id=state)
            #알람도 추가해야함.
            machine_done_webpush(state, reserve_lst)
            state.save()