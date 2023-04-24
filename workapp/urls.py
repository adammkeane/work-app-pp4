from . import views
from django.urls import path

urlpatterns = [
    path('', views.BulletinHome.as_view(), name='bulletin_home'),
    path(
        'services/', views.PostListService.as_view(), name='bulletin_services'
        ),
    path(
        'requests/', views.PostListRequest.as_view(), name='bulletin_requests'
        ),
    path(
        '<slug:slug>/<slug:id>/', views.PostDetail.as_view(),
        name='post_detail'
        ),
]
