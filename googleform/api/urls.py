from index.views import FormAPI
from django.urls import path

urlpatterns = [
    path('form/', FormAPI.as_view()),

]