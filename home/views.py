from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


def logout_user(request):
    logout(request)
    return redirect('/login')

@login_required
def home_page(request,username):
    template = loader.get_template('all_polls.html')
    context = {}
    return HttpResponse(template.render(context,request))


    
