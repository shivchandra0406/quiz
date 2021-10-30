from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializer import *

from .models import *
# Create your views here.
class UserView(APIView):
    def Post(self,request):
        try:
            data=request.data
            serializer=BaseSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status':'Success',
                    'data':serializer.data
                })
            return Response({
                'status':'False',
                'message':serializer.errors
            })
        except Exception as e:
            return Response({
                'status':'False',
                'message':'somthing went wrong'
            })




class QuizRedyView(APIView):
    def get(self,request):
        try:
            print("skalghkl;agh;agldfhal")
            data=request.data
            checkserializer=SimpleQuizSerializer(data=data)
            if checkserializer.is_valid():
                print("shhivlskglks")
                obj=Question.objects.filter(category__category_name=checkserializer.data['category_name'])[0:checkserializer.data['question_limit']]

                if len(obj)<0:
                    return Response({
                        'status':"False",
                        'message':'you have wrong fill category name'
                    })
                serializer=QusetionSerializer(obj,many=True)
                print(serializer)
                return Response({
                    'message':serializer.data
                })
            return Response({
                    'message':checkserializer.errors
                })
        except Exception as e:
            print(e)
            return Response({
                'message':'somthing went wrong'
            })
    def post(self,request):
        try:
            data=request.data
            serializer=SimpleSerializer(data=data)
            if serializer.is_valid():
                obj=Question.objects.filter(uid=serializer.data['question_id']).first()
                print(obj)
                if obj is None:
                    return Response({
                        'status':'False',
                        'message':'Question is not valid'
                    })

                if obj.answers.filter(answer=serializer.data['answer']).exists():

                    answer=obj.answers.filter(answer=serializer.data['answer'],is_correct=True).first()
                    user=User.objects.filter(id=serializer.data['user_id']).first()

                    
                    if answer is not None:
                        user=User.objects.filter(id=serializer.data['user_id']).first()
                        # print('user',user)
                        # totalmarks=user.storequiz.filter(user__id=serializer.data['id']).first()
                        store=StoreQuiz.objects.filter(user__id=serializer.data['user_id']).first()
                        print("agskjslgds",store.totalmarks)

                        if store is None:
                            StoreQuiz.objects.create(
                            totalmarks=2,
                            user=user,
                            question=answer,
                            youranswer=True
                            )
                            return Response({
                                    'status':'Success',
                                    'message':'Your answer is correct'
                                })
                        else:
                            StoreQuiz.objects.create(
                            totalmarks=2,
                            user=user,
                            question=answer,
                            youranswer=True
                            )
                            return Response({
                                    'status':'Success',
                                    'message':'Your answer is correct'
                                    })
                    else: 
                        StoreQuiz.objects.create(
                            totalmarks=-2,
                            user=user,
                            question=answer,
                            youranswer=True
                            )           
                        return Response({
                            'status':'False',
                            'message':'Your answer is not correct'
                        })
                return Response({
                    'status':'False',
                    'message':'option is not valid'
                })
            return Response({
                'status':'False',
                'message':serializer.errors
            })
        except Exception as e:
            print(e)
            return Response({
                'status':'False',
                'message':'somthing went wrong'
            })
class UserView(APIView):
    def get(self,request):
        try:
            id=request.GET.get('id')
            obj=User.objects.filter(id=id).first()
        
            if obj is None:
                return Response({
                    'message':'no user found'
                })
            obj1=obj.storequiz.all()
            print("skjdgl;jlg;",obj1)
            # obj2=StoreQuiz.objects.filter(user__id=id).first()
            # print("ks;adgkj;lsaj",obj2)
            serializer=UserSerializer(obj)
            return Response({
                'message':serializer.data
            })
        except Exception as e:
            print(e)
            return Response({
                'message':'somthing went wrong'
            })
