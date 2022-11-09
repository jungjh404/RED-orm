from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from common.forms import UserForm
from django.views.decorators.http import require_POST
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def main (request) :
    context = {}
    return render (request, 'common/main.html', context)

# def login (request) :
#     return HttpResponse("로그인 페이지입니다.")

# def signup (request) :
#     if request.method == "POST" :
#         form = UserForm(request.POST)
#         if form.is_valid() :
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password) #사용자 인증
#             login(request, user)
#             return redirect('dorms:index')
#         else :
#             form = UserForm()
#     return render (request, 'common/signup.html', {'form':form})

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('dorms:index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})

# @require_POST
# def delete (request) :
#     if request.user.is_authenticated :
#         request.user.delete()
#         auth_logout(request)
#     return redirect('common:main')