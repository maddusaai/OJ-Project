from django.urls import path,include
<<<<<<< HEAD
from home.views import logout_user,home_page,problem_page,leaderboard,submit
=======
from home.views import logout_user,home_page,problem_page,leaderboard
>>>>>>> 98d50a609e1835aebd0973b96848003db8f2acc3

urlpatterns = [
  path("logout/",logout_user,name = "logout_user"),
  path("home/",home_page,name = "home-page"),
  path("problem/<str:name>/",problem_page,name="problem_page"),
<<<<<<< HEAD
  path("leaderboard/",leaderboard,name="leader_board"),
  path("submit/<str:ques_name>/",submit,name = "submit_code")
=======
  path("leaderboard/",leaderboard,name="leader_board")
>>>>>>> 98d50a609e1835aebd0973b96848003db8f2acc3
]