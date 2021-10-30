from django.db.models import fields
from rest_framework import serializers
from .models import * 
class CourseSerializer(serializers.ModelSerializer):
    course_name=serializers.CharField(required=True)
    class Meta:
        model=Course
        fields='__all__'

class QuestionSerializer(serializers.ModelSerializer):
    # question=serializers.CharField(required=True)
    # option1=serializers.CharField(required=True)
    # option2=serializers.CharField(required=True)
    # option3=serializers.CharField(required=True)
    # option4=serializers.CharField(required=True)
    class Meta:
        model=Question
        fields='__all__'

class CourseSerializer1(serializers.ModelSerializer):
    ques=QuestionSerializer(read_only=True,many=True)
    
    class Meta:
        model=Course
        fields=['id','course_name','ques']
        dept=1
        


