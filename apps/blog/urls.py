from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list_view, name='blog'),
    path('detail/', views.blog_detail_view, name='blog_detail'),
]
