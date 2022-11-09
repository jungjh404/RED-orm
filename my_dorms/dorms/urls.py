from django.urls import path
from . import views

app_name = 'dorms'

urlpatterns = [
    path ('', views.index, name='index'),
    path ('<int:context_id>/', views.detail, name='detail'),
    path ('comment/create/<int:context_id>/', views.comment_create, name='comment_create'),
    path ('context/create/', views.context_create, name = 'context_create'),
    path ('context/modify/<int:context_id>/', views.context_modify, name='context_modify'),
    path ('info/', views.info_index, name='info_index'),
    path ('info/<int:context_id>/', views.info_detail, name='info_detail'),
    path ('info/comment/create/<int:context_id>/', views.info_comment_create, name='info_comment_create'),
    path ('info/context/create/', views.info_context_create, name = 'info_context_create'),
    path ('info/context/modify/<int:context_id>/', views.info_context_modify, name='info_context_modify'),
    path ('free/', views.free_index, name='free_index'),
    path ('free/<int:context_id>/', views.free_detail, name='free_detail'),
    path ('free/comment/create/<int:context_id>/', views.free_comment_create, name='free_comment_create'),
    path ('free/context/create/', views.free_context_create, name = 'free_context_create'),
    path ('free/context/modify/<int:context_id>/', views.free_context_modify, name='free_context_modify'),
    path ('trade/', views.trade_index, name='trade_index'),
    path ('trade/<int:context_id>/', views.trade_detail, name='trade_detail'),
    path ('trade/comment/create/<int:context_id>/', views.trade_comment_create, name='trade_comment_create'),
    path ('trade/context/create/', views.trade_context_create, name = 'trade_context_create'),
    path ('trade/context/modify/<int:context_id>/', views.trade_context_modify, name='trade_context_modify'),
    path ('copurchase/', views.copurchase_index, name='copurchase_index'),
    path ('copurchase/<int:context_id>/', views.copurchase_detail, name='copurchase_detail'),
    path ('copurchase/comment/create/<int:context_id>/', views.copurchase_comment_create, name='copurchase_comment_create'),
    path ('copurchase/context/create/', views.copurchase_context_create, name = 'copurchase_context_create'),
    path ('copurchase/context/modify/<int:context_id>/', views.copurchase_context_modify, name='copurchase_context_modify'),
]