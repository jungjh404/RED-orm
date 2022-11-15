from django.urls import path
from . import views

app_name = 'washing_machine'

urlpatterns = [
    path('', views.status, name='status'),
    path('camera/', views.camera, name='camera'),
]