from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.mainView, name="mainView"),
    path('register/', views.userRegister, name='userRegister'),
    path('login/', views.loginUser, name='loginUser'),
    path('logout/', views.logOut, name='logOut'),
    path('own/', views.ownUserProfile, name='ownUserProfile'),
    path('publish/', views.publishPost, name='publishPost'),
    path('userSettings/', views.userSettings, name='userSettings'),
    path('user/<str:p_username>/', views.requestedUserProfile, name='requestedUserProfile'),
    path('delete/<int:p_pid>/',views.deletePost, name='deletePost'),
]
