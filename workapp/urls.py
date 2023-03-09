from . import views
from django.urls import path
import random

urlpatterns = [
    path('', views.PostList.as_view(), name='bulletin'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]