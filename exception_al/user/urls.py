from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.CustomUserList.as_view()),
    path('user/register', views.CustomUserRegister.as_view()),
    path('user/<int:pk>/', views.CustomUserDetail.as_view()),
    path('user/change_password/<int:pk>/', views.ChangePasswordView.as_view()),
    path('user/check_username/', views.CheckUsernameView.as_view()),
]