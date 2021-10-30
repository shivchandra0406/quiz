from django.urls import path
from .views import *
urlpatterns = [
    
    path('',courseView1),
    #path('getcourse/',CourseView.as_view()),

    path('<id>',take_quiz,name="take_quiz"),
    path('addquestion/',QuestionView.as_view())
]