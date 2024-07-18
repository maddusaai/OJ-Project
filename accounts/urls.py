from django.urls import path,include
from accounts.views import login_user,register_user

urlpatterns = [
  path("register/",register_user,name = "register-user"),
  path("login/",login_user,name = "login-user"),
]