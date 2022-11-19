from django.db import models
from core import models as core_models

class Room(core_models.TimeStampedModel):
    class Meta:
        db_table = "room"

class Conversation(core_models.TimeStampedModel):
    
    user_id = models.ForeignKey(
        "common.User", related_name="conversations", on_delete=models.CASCADE, db_column='user_id'
    )

    room_id= models.ForeignKey(Room, on_delete=models.CASCADE, related_name="conversations", db_column="room_id")
    
    class Meta:
        db_table='conversations'
    


class Message(core_models.TimeStampedModel):
    message = models.CharField(max_length=500)
    user_id = models.ForeignKey("common.User", related_name="message", on_delete=models.CASCADE, db_column='user_id')
    room_id= models.ForeignKey(Room, on_delete=models.CASCADE, related_name="message", db_column="room_id")

    class Meta:
        db_table = "message"

    def __str__(self):
        return f"{self.user} says: {self.message}"

    def last_30_messages(self, room_id):
        return Message.objects.filter(room_id=room_id).order_by('created')[:30]