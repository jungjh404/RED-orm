from django.shortcuts import render, get_object_or_404, redirect
from .models import Washing_Machine, Usage_Status, Reservation
from django.contrib.auth.decorators import login_required


# Create your views here.
def status(request):
    machine_lst = Washing_Machine.objects.all()
    machine_form = {
        "machine_lst": machine_lst
    }
    return render(request, 'washing_machine/status.html', machine_form)
