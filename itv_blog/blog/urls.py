from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.registration_view, name='register'),
    path('posts/', views.post_list_view, name='post_list'),
    path('posts/<int:post_id>/', views.post_detail_view, name='post_detail'),
]
