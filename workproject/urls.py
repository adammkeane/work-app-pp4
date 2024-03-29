"""workproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from workapp import views
from home import views as views_home

urlpatterns = [
    path('', views_home.HomePage.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('bulletin/', include('workapp.urls'), name='workapp_urls'),
    path('accounts/', include('allauth.urls')),
    path('profile/<slug:user>/', views.ProfilePage.as_view(), name='profile'),
    path('post_create/', views.PostCreate.as_view(), name='post_create'),
    path(
        'post_edit/<slug:post_id>/', views.PostEdit.as_view(), name='post_edit'
        ),
    path(
        'post_delete/<slug:post_id>/', views.PostDelete.as_view(),
        name='post_delete'
        ),
    path(
        'post_review_create/<slug:post_id>/', views.PostReviewCreate.as_view(),
        name='post_review_create'
        ),
]
