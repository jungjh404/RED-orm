from django.urls import path
from . import views

app_name = 'dorms'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:context_id>/', views.detail, name='detail'),
    path ('comment/create/<int:context_id>/', views.comment_create, name='comment_create'),
    path ('context/create/', views.context_create, name = 'context_create'),
]