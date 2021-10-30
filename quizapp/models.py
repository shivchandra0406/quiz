from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.
class BaseModel(models.Model):
    uid=models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    class Meta:
        abstract=True
class Category(BaseModel):
    category_name=models.CharField(max_length=100)
    def __str__(self):
        return self.category_name
class Question(BaseModel):
    question=models.CharField(max_length=100)
    marks=models.IntegerField(default=2)
    category=models.ForeignKey(Category,related_name='questions',on_delete=models.CASCADE)
   
class Answerss(BaseModel):
    question=models.ForeignKey(Question,related_name='answers',on_delete=models.CASCADE)
    answer=models.CharField(max_length=100)
    is_correct=models.BooleanField(default=False)

class StoreQuiz(BaseModel):
    totalmarks=models.IntegerField(default=0)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='storequiz')
    question=models.OneToOneField(Answerss,related_name='ansstorequiz',on_delete=models.CASCADE)
    youranswer=models.BooleanField()


# class QuizRedy(BaseModel):
#     category=models.ForeignKey(Category,related_name='catquiz',on_delete=models.CASCADE)
#     questions=models.ForeignKey(Question,related_name='quizquestins',on_delete=models.CASCADE)
# 
#     answer=models.ForeignKey(Answerss,related_name='quizanswer',on_delete=models.CASCADE)
# class Quiz(BaseModel):
#     category=models.ForeignKey(Category,on_delete=models.CASCADE)
#     question_limit=models.IntegerField(default=10)
#     quiz_name=models.CharField(max_length=100,null=True,blank=True)

# class QuizQuestion(BaseModel):
#     quiz=models.ForeignKey(Quiz,on_delete=models.CASCADE,related_name='quiz_questions')
#     question=models.ForeignKey(Question,on_delete=models.CASCADE)