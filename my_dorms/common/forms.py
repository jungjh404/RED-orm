from django.contrib.auth.forms import UserChangeForm

class UserForm(UserCreationForm):
    class Meta :
        model = User()
        fields = ["username", "password1", "password2", "name",
                  "gender","building", "room_num"]

class CustomUserChangeForm (UserChangeForm) :
    password = None
    name = forms.CharField(label='name', widget=forms.TextInput(
        attrs={'class': 'form-control', 'maxlength': '200', }),
        )
    GENDER_CHOICES = (
        ("여학생", "여학생"),
        ("남학생", "남학생"),
    )
    gender = forms.ChoiceField(choices = GENDER_CHOICES, label='gender', widget=forms.TextInput(
        attrs={'class': 'form-control', 'maxlength':'8',} ),
        )
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
    building = forms.ChoiceField(choices = BD_CHOICES, label='building', widget = forms.TextInput (
      attrs = {'class': 'form-control', 'maxlength': '100', }),),
    room_num = forms.IntegerField(label='room_num', widget=forms.NumberInput(
        attrs={'class': 'form-control', 'maxlength':'11',}),
    )

    class Meta :
        model = User()
        fields = ['name', 'gender', 'building', 'room_num']