from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse

from django.shortcuts import redirect, reverse, render
from conversations.services.chat_room_service import get_an_chat_room_list, get_chat_room_user, confirm_user_chat_room_join
from conversations.services.message_service import get_an_message_list



#로그인 안할시 로그인 페이지로 이동
@login_required(login_url='common:login')
def chat_view(request: HttpRequest) -> HttpResponse:
    # 사용자의 존재 여부 확인
    user = request.user.is_authenticated
    # 사용자가 있으면 사용자가 속해있는 채팅방 list 표시
    if user:
        # 유저가 참여하고 있는 채팅방 목록(Conversations query)
        chat_room_list = get_an_chat_room_list(request.user.id)
        chat_info = {}
        for chat_room in chat_room_list:
            room_id = chat_room.room_id.id
            # 채팅방에 참여중인 유저 list(Conversations query)
            chat_user_list = get_chat_room_user(room_id)

            username_list = []
            building_info = ''
            roomNum_info = ''
            for chat_user in chat_user_list:
                username = chat_user.user_id.username
                building_info = chat_user.user_id.building
                roomNum_info = chat_user.user_id.room_num
                username_list.append(username)
            # chat_info 변수에 딕셔너리 형태로 저장
            # building_info 및 roomNumber 를 더해 리스트 구성
            username_list.append(building_info)
            username_list.append(roomNum_info)
            chat_info[room_id] = username_list

        if chat_info == {}:
            chat_info = None

        return render(request, "conversations/chat.html", {'chat_info': chat_info})
    # 사용자가 없는 경우 로그인화면
    else:
        return redirect(("/common/login"))

@login_required(login_url='common:login')
def room_view(request: HttpRequest, room_name: str) -> HttpResponse:
    room_id = int(room_name)
    try:
        confirm_user_chat_room_join(request.user.id, room_id)
        
        message = get_an_message_list(room_id)

        return render(request, "conversations/room.html", {"room_name": room_name, "message": message, "user_name": request.user.username})

    except:
        return redirect(("/conversations"))

