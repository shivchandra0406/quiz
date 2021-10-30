from django.urls import path
from .views import *
urlpatterns = [
     path('quiz/',QuizRedyView.as_view()),
     path('user/',UserView.as_view()),
     
]