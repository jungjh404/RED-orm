from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'common'

urlpatterns=[
    path('main/', views.main, name='main'),
    path('login/', auth_views.LoginView.as_view(template_name = "common/login.html"), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('show/', views.profile_view, name='show'),
    path('show/update/', views.profile_update_view, name='profile_update'),
]