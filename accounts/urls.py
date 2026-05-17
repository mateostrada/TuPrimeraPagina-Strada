from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView,PasswordChangeView
from accounts.views import *

urlpatterns = [
    path("login/",LoginView.as_view(template_name="accounts/login.html"),name="login"),
    path("logout/", LogoutView.as_view(template_name="accounts/logout.html"),name="logout"),
    path("register/",register,name="register"),
    path("profile/",profile_detail,name="profile_detail"),
    path("profile/change",profile_change,name="profile_change"),
    path("password/change/",PasswordChangeView.as_view(template_name="accounts/password_change.html"),name="password_change"),
]