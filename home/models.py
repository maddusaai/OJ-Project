from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class user_questions_solved(models.Model):
  solver = models.OneToOneField(User, on_delete=models.CASCADE)
  no_of_questions = models.IntegerField(default=0)

class question_details(models.Model):
  DIFFICULTY_CHOICES = [
      ('Easy', 'Easy'),
      ('Medium', 'Medium'),
      ('Hard', 'Hard'),
  ]

  name = models.CharField(max_length=200)
  description = models.TextField()
  difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default='Easy')
  sample_input = models.TextField()
  sample_output = models.TextField()
  constraints = models.TextField()

class user_question_details(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  problem = models.ForeignKey(question_details, on_delete=models.CASCADE)
  solved = models.BooleanField(default=False)
