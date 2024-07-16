from django.urls import path,include
from home.views import logout_user,home_page,problem_page,leaderboard

urlpatterns = [
  path("logout/",logout_user,name = "logout_user"),
  path("home/",home_page,name = "home-page"),
  path("problem/<str:name>/",problem_page,name="problem_page"),
  path("leaderboard/",leaderboard,name="leader_board")
]