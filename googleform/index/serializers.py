from rest_framework import serializers
from .models import (
    Form,
    Choices,
    Questions,
    Answers,
    Response
)
class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        exclude = ['created_at', 'updated_at']
class ChoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choices
        exclude = ['created_at', 'updated_at']
class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        exclude = ['created_at', 'updated_at']
class AnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answers
        exclude = ['created_at', 'updated_at']
class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Response
        exclude = ['created_at', 'updated_at']