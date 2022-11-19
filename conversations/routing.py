from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r"ws/conversations/(?P<room_name>\w+)/$", consumers.ConversationsConsumer.as_asgi()),
]