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
class Dormmate_offer(TimeStampedModel):
    pass

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