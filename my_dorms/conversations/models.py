from django.db import models
from core import models as core_models

class Conversation (core_models.TimeStampedModel):
    
    participants = models.ManyToManyField(
        "common.User", related_name="conversations", blank=True,
    )
    def __str__(self):
        usernames = []
        usernames.append(self.sender_id)
        usernames.append(self.receiver_id)
        return ",  ".join(usernames)


    def count_messages(self):
        self.messages.count()
    


class Message(core_models.TimeStampedModel):
    message = models.TextField
    user = models.ForeignKey("common.User", related_name="message", on_delete=models.CASCADE)
    conversation = models.ForeignKey('Conversation', related_name="messages",on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.user} says: {self.message}"