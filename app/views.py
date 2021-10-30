from django.shortcuts import render
from rest_framework.response import Response
from .serializer import * 
from .models import *
from rest_framework.views import  APIView
# Create your views here.
#import requests
def courseView1(request):
    try:
        obj=Course.objects.all()
        d={'courses':obj}
        return render(request,'app/home.html',context=d)
    except Exception as e:
        print(e)
        

def take_quiz(request,id):
    d={'course_id':id}
    return render(request,'app/quiz.html',context=d)
class CourseView(APIView):
    def post(self,request):
        try:
            data=request.data
            serializer=CourseSerializer(data=data)
            if serializer.is_valid():
                return Response({
                    'status':'Success',
                    'details':serializer.data
                })
            return Response({
               'status':'Failure',
               'details':serializer.errors 
            })
    
        except Exception as e:
            print(e)
            return Response({
                'status':'error',
                'details':'somthing went wrong'
            })
    def get(self,request):
        try:
            id=request.GET.get('id')
            print('______________-',id)
            data=Question.objects.filter(course_id=id)
            print(data)
            serializer=QuestionSerializer(data,many=True)
            return render(request,'index.html',{'response':serializer.data})
            # return Response({
            #         'status':'Success',
            #         'details':serializer.data
            #     })
            
        except Exception as e:
            print(e)
            return Response({
                'status':'error',
                'details':'somthing went wrong'
            })

    
        
class QuestionView(APIView):
    def post(self,request):
        try:
            data=request.data
            serializer=QuestionSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status':'Success',
                    'details':serializer.data
                })
            return Response({
               'status':'Failure',
               'details':serializer.errors 
            })
        except Exception as e:
            print(e)
            return Response({
                'status':'error',
                'details':'somthing went wrong'
            })
    def get(self,request):
        id=request.GET.get('id')
        data=Question.objects.get(id=id)
        serializer=QuestionSerializer(data)
        return Response({
            'status':'Success',
            'details':serializer.data
        })
    

