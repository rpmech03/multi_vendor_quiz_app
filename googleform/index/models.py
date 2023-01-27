from django.db import models
from django.contrib.auth.models import User, AbstractUser
from .choices import QUESTION_CHOICES

class User(AbstractUser, models.Model):
    email = models.EmailField(unique = True)

class BaseModel(models.Model):
    # uuid = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True

class Choices(BaseModel):
    choice = models.CharField(max_length=100)

    class Meta:
        db_table = "choices"
        ordering = ['-choice']

class Questions(BaseModel):
    question = models.CharField(max_length=100)
    question_type = models.CharField(choices = QUESTION_CHOICES, max_length=100)
    required = models.BooleanField(default=False)
    choices = models.ManyToManyField(Choices, related_name= "question_choices", blank=True)


class Form(BaseModel):
    code = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    background_color = models.CharField(max_length=100, default = "#272124")
    collect_email = models.BooleanField(default=False)
    questions = models.ManyToManyField(Questions, related_name= "questions")

class Answers(BaseModel):
    answer = models.CharField(max_length=100)
    answer_to = models.ForeignKey(Questions, on_delete=models.CASCADE, related_name= "answer_to")

class Response(BaseModel):
    response_code = models.CharField(max_length=100, unique= True)
    response_to = models.ForeignKey(Form, on_delete= models.CASCADE)
    responder_id = models.CharField(max_length=100)
    responder_email = models.EmailField(null= True, blank=True)
    response = models.ManyToManyField(Answers, related_name= "answers")