from django.contrib import admin
from .models import Washing_Machine, Usage_Status, Reservation

# Register your models here.
admin.site.register(Washing_Machine)
admin.site.register(Usage_Status)
admin.site.register(Reservation)