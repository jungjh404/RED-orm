from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    name = forms.CharField(max_length=50, label="이름")
    building = forms.IntegerField(label="기숙사 건물")
    room = forms.IntegerField(label="기숙사 방")

    class Meta :
        model = User
        fields = ("username", "password1", "password2", "name", "building", "room")