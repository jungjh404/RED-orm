from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.
class Washing_Machine(models.Model):
    machine_id = models.IntegerField()
    building = models.CharField(max_length=1)
    floor = models.IntegerField()
    room = models.IntegerField()

    def __str__(self):
        return f'{self.building} {self.floor} {self.room}'


class Usage_Status(models.Model):
    machine_id = models.ForeignKey(Washing_Machine, on_delete=models.PROTECT)
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    start_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f'{self.machine_id} {self.user_id}'


class Reservation(models.Model):
    machine_id = models.ForeignKey(Washing_Machine, on_delete=models.PROTECT)
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    reservation_time = models.DateTimeField()
    
    def __str__(self):
        return f'{self.machine_id} {self.user_id}'