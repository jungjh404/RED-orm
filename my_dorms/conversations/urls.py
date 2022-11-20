from django.urls import path
from . import views

app_name = "conversations"

urlpatterns = [
    path('', views.chat_view, name='conversations'),
    path("<str:room_name>/", views.room_view, name="room"),  # /conversations/room_number/ 으로 넘어오면 room 함수 실행
]