from django.urls import path
from . import views

app_name = 'washing_machine'

urlpatterns = [
    path('', views.status, name='status'),
    path('camera/', views.camera, name='camera'),
    path('reserve_camera/', views.reserve_camera, name='reserve_camera'),
    path('add/', views.add, name='add'),
    path('reserve/', views.reserve, name='reserve'),
]