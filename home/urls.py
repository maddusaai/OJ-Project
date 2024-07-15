from django.urls import path,include
from home.views import logout_user,home_page

urlpatterns = [
  path("logout/",logout_user,name = "logout_user"),
  path("home/<str:username>",home_page,name = "home-page")
]