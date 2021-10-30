from django.db import models



class Course(models.Model):
    course_name=models.CharField(max_length=50)
    def __str__(self) :
        return self.course_name
class Question(models.Model):
    course=models.ForeignKey(Course,related_name='ques',on_delete=models.CASCADE)
    question=models.CharField(max_length=100)
    option1=models.CharField(max_length=100)
    option2=models.CharField(max_length=50)
    option3=models.CharField(max_length=50)
    option4=models.CharField(max_length=50)
    answer=models.IntegerField()
    

    