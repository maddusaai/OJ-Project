from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import user_questions_solved,question_details,user_question_details
from django.contrib.auth.models import User


def logout_user(request):
    logout(request)
    return redirect('/login')

@login_required
# views.py



def home_page(request):
    user_questions, created = user_questions_solved.objects.get_or_create(solver=request.user)
    
    x=question_details.objects.all()
    context = {
        'nops': user_questions.no_of_questions,
        'data_from_another_model':x
    }
    return render(request, 'all_polls.html', context)

@login_required

def problem_page(request, name):
    problem = get_object_or_404(question_details, name=name)
    context={
        'ques_name':problem.name,
        'desc':problem.description,
        'samp_in':problem.sample_input,
        'samp_out':problem.sample_output
    }
    return render(request, 'question_view.html',context)

def leaderboard(request):
    users = User.objects.all()
    leaderboard_data = []

    for user in users:
        solved_count = user_question_details.objects.filter(user=user, solved=True).count()
        leaderboard_data.append({
            'username': user.username,
            'solved_count': solved_count
        })

    # Sort by solved_count in descending order
    leaderboard_data = sorted(leaderboard_data, key=lambda x: x['solved_count'], reverse=True)

    return render(request, 'leader_board.html', {'leaderboard_data': leaderboard_data})