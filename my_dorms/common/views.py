from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import UserForm, CustomUserChangeForm
from .models import User
from dorms.models import Context
from conversations.services.chat_room_service import get_an_chat_room_list, get_chat_room_user, confirm_user_chat_room_join, \
    creat_an_chat_room, creat_an_room_join

# Create your views here.
def main (request) :
    context_list = Context.objects.all()[:5]
    context = {
        'context_list' : context_list
    }
    return render (request, 'common/main.html', context)

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            #이웃한 방 유저 체크하고 메시지 room 생성
            try: 
                neighbor1 = User.objects.get(building=user.building, room_num=user.room_num+1)
                room = creat_an_chat_room()
                room_id = room.id
                creat_an_room_join(user, neighbor1, room)
                
            except User.DoesNotExist:
                neighbor1 = None
            try: 
                neighbor2 = User.objects.get(building=user.building, room_num=user.room_num-1)
                room = creat_an_chat_room()
                room_id = room.id
                creat_an_room_join(user, neighbor2, room)
            except User.DoesNotExist:
                neighbor2 = None

            



            login(request, user)  # 로그인
            return redirect('common:main')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})

def profile_view (request) :
    if request.method == 'GET' :
        return render (request, 'common/profile.html')

def profile_update_view(request) :
    if request.method == 'POST' :
        user_change_form = CustomUserChangeForm(request.POST, instance=request.user)

        if user_change_form.is_valid() :
            user = user_change_form.save()
            user.save()
            return render (request, 'common/profile.html')

    else :
        user_change_form = CustomUserChangeForm(instance=request.user)

    return render (request, 'common/profile_update.html', {'user_change_form':user_change_form})
