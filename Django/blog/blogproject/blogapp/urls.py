from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.Postlist.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]