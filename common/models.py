from django.db import models
from django.contrib.auth.models import AbstractUser

class User (AbstractUser) :
    name = models.CharField(max_length = 200)
    GENDER_CHOICES = (
        ("여학생", "여학생"),
        ("남학생", "남학생"),
    )
    gender = models.CharField(choices = GENDER_CHOICES, max_length = 50)
    BD_CHOICES = (
        ("신관A", "신관A"),
        ("신관B", "신관B"),
        ("인관", "인관"),
        ("의관", "의관"),
        ("예관", "예관"),
        ("지관", "지관"),
        ("C하우스", "C하우스"),
        ("E하우스-본관", "E하우스-별관"),
        ("G하우스", "G하우스"),
        ("I하우스", "I하우스"),
        ("K하우스", "K하우스"),
        ("M하우스-A동", "M하우스-A동"),
        ("M하우스-B동", "M하우스-B동"),
        ("빅토리하우스", "빅토리하우스"),
        ("이완근관", "이완근관"),
        ("크라운빌-A동", "크라운빌-A동"),
        ("크라운빌-C동", "크라운빌-C동"),
    )
    building = models.CharField(choices=BD_CHOICES, max_length=100)
    room_num = models.IntegerField(null=True)