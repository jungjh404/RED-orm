from django.db import models
from django.contrib.auth import get_user_model
from core.models import TimeStampedModel
User = get_user_model()
# Create your models here.
class Context (models.Model) :
    writer = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    title = models.CharField(max_length = 100)
    date = models.DateTimeField()
    content = models.TextField()
    modify_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

class Comment (models.Model) :
    context = models.ForeignKey(Context, on_delete=models.CASCADE)
    content = models.TextField(null = False)
    writer = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.content


#정보
class Context_info (models.Model) :
    writer = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    title = models.CharField(max_length = 100)
    date = models.DateTimeField()
    content = models.TextField()
    modify_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

class Comment_info (models.Model) :
    context = models.ForeignKey(Context_info, on_delete=models.CASCADE)
    content = models.TextField(null = False)
    writer = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.content

#자유
class Context_free (models.Model) :
    writer = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    title = models.CharField(max_length = 100)
    date = models.DateTimeField()
    content = models.TextField()
    modify_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

class Comment_free (models.Model) :
    context = models.ForeignKey(Context_free, on_delete=models.CASCADE)
    content = models.TextField(null = False)
    writer = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.content

#물품 거래

class Context_trade (models.Model) :
    writer = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    title = models.CharField(max_length = 100)
    date = models.DateTimeField()
    content = models.TextField()
    modify_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

class Comment_trade (models.Model) :
    context = models.ForeignKey(Context_trade, on_delete=models.CASCADE)
    content = models.TextField(null = False)
    writer = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.content


#돔메 구인
class Context_dormmate(models.Model):
    writer = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    title = models.CharField(max_length = 100)
    date = models.DateTimeField()
    content = models.TextField()
    modify_date = models.DateTimeField(null=True, blank=True)
    isSnoring = models.BooleanField(null = True, blank=True)
    time_awake_1 = models.IntegerField(null = True, blank= True)
    time_awake_2 = models.IntegerField(null = True, blank= True)
    time_sleep_1 = models.IntegerField(null = True, blank= True)
    time_sleep_2 = models.IntegerField(null = True, blank= True)
    isSmoking = models.BooleanField(null = True, blank=True)
    age = models.IntegerField( null = True, blank =True)
    usingPC = models.BooleanField(null = True, blank=True)
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

    def __str__(self):
        return self.content

class Comment_dormmate (models.Model) :
    context = models.ForeignKey(Context_dormmate, on_delete=models.CASCADE)
    content = models.TextField(null = False)
    writer = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.content

#공동 구매
class Context_copur (models.Model) :
    writer = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    title = models.CharField(max_length = 100)
    date = models.DateTimeField()
    content = models.TextField()
    modify_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

class Comment_copur (models.Model) :
    context = models.ForeignKey(Context_copur, on_delete=models.CASCADE)
    content = models.TextField(null = False)
    writer = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.content