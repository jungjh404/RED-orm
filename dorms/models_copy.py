from django.db import models

# Create your models here.
class Context (models.Model) :
    writer = models.ForeignKey("common.User", on_delete=models.PROTECT, null=True)
    title = models.CharField(max_length = 100)
    date = models.DateTimeField()
    content = models.TextField()

    def __str__(self):
        return self.title

class Comment (models.Model) :
    context = models.ForeignKey(Context, on_delete=models.CASCADE)
    content = models.TextField()
    writer = models.ForeignKey("common.User", on_delete=models.PROTECT, null=True)
    create_date = models.DateTimeField()

    def __str__(self):
        return self.content