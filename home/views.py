from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import user_questions_solved,question_details,user_question_details
from django.contrib.auth.models import User
<<<<<<< HEAD
from home.forms import CodeSubmissionForm
from django.conf import settings
from pathlib import Path
import os
import uuid
import subprocess
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError
=======
>>>>>>> 98d50a609e1835aebd0973b96848003db8f2acc3


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

<<<<<<< HEAD
def problem_page(request,name):
    problem = get_object_or_404(question_details, name=name)
    form = CodeSubmissionForm()
    context={
        'form':form,
=======
def problem_page(request, name):
    problem = get_object_or_404(question_details, name=name)
    context={
>>>>>>> 98d50a609e1835aebd0973b96848003db8f2acc3
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

<<<<<<< HEAD
    return render(request, 'leader_board.html', {'leaderboard_data': leaderboard_data})




def validate_input(data):
    try:
        int(data)
        return True
    except ValueError:
        return False

@csrf_exempt
def submit(request,ques_name):
    if request.method == "POST":
        form = CodeSubmissionForm(request.POST)
        
        print(ques_name)
        if form.is_valid():
            input_data = form.cleaned_data.get('input_data', '').strip().split('\n')

            if all(validate_input(data) for data in input_data):
                submission = form.save()
                output = run_code(submission.language, submission.code, '\n'.join(input_data),ques_name)
                submission.output_data = output
                submission.save()
                return JsonResponse({'success': True, 'output_data': output})
            else:
                return JsonResponse({'success': False, 'error': 'Invalid input data.'})
        else:
            return JsonResponse({'success': False, 'error': form.errors.as_json()})
    return JsonResponse({'success': False, 'error': 'Invalid request method.'})


        
def run_code(language, code, input_data,ques_name):
    project_path = Path(settings.BASE_DIR)
    directories = ["codes", "inputs", "outputs"]
    input_lines = input_data.strip().split('\n')
    cleaned_input_data = '\n'.join(line.strip() for line in input_lines)

    for directory in directories:
        dir_path = project_path / directory
        if not dir_path.exists():
            dir_path.mkdir(parents=True, exist_ok=True)
    
    codes_dir = project_path / "codes"
    input_dir = project_path / "inputs"
    output_dir = project_path / "outputs"

    unique = str(uuid.uuid4())
    

    code_file_name = f"{unique}.{language}"
    input_file_name = f"{ques_name}_input.txt"
    output_file_name = f"{unique}.txt"
    output_file_test_case = f"{ques_name}_output.txt"
    
    code_file_path = codes_dir / code_file_name
    input_file_path = input_dir / input_file_name
    output_file_path = output_dir / output_file_name
    output_file_path_test_case = output_dir / output_file_test_case

    # Write code to file
    with open(code_file_path, "w") as code_file:
        code_file.write(code)

    #Write input data to file
    with open(input_file_path, "w") as input_file:
        input_file.write(cleaned_input_data)

    if language == "cpp":
        executable_path = codes_dir / unique
        compile_result = subprocess.run(
            ["g++", str(code_file_path), "-o", str(executable_path)]
        )

        if compile_result.returncode == 0:
            with open(output_file_path, "w") as output_file:
                subprocess.run(
                    [str(executable_path)],
                    stdin=open(input_file_path, "r"),
                    stdout=output_file
                )

    elif language == "py":
        with open(output_file_path, "w") as output_file:
            subprocess.run(
                ["python3", str(code_file_path)],
                stdin=open(input_file_path, "r"),
                stdout=output_file
            )

    # Read the output from the output file
    with open(output_file_path, "r") as output_file:
        output_data = output_file.read()
    
    with open(output_file_path_test_case,"r") as output_file_2:
        output_data_test_case = output_file_2.read()
    
    if(output_data == output_data_test_case):
        return True
    
    return False

    # return output_data


def compare_files(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        content1 = f1.read()
        content2 = f2.read()
    
    return content1 == content2


=======
    return render(request, 'leader_board.html', {'leaderboard_data': leaderboard_data})
>>>>>>> 98d50a609e1835aebd0973b96848003db8f2acc3
