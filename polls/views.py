from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView, status, Response
from . import models
from . import serializers


class GetQuestionData(APIView):
    def get(self, request):
        query = models.Question.objects.all()
        serializer = serializers.QuestionModelSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GetChoiseData(APIView):
    def get(self, request):
        query = models.Choise.objects.all()
        serializer = serializers.ChoiseModelSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UpdateQuestion(APIView):
    def put(self, request, pk):
        query = models.Question.objects.get(pk=pk)
        serializer = serializers.QuestionModelSerializer(query, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostData(APIView):
    def post(self, request):
        serializer = serializers.QuestionModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Search(APIView):
    def get(self, request):
        search = request.GET['name']
        query = models.Question.objects.filter(question_text__contains=search)
        serializer = serializers.QuestionModelSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def searchDef(request):
    if request.method =='GET':
        query=models.Question.objects.all().order_by('-pub_date')
        serializer=serializers.QuestionModelSerializer(query,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)



class DeleteData(APIView):
    def delete(self,request,pk):
        query=models.Question.objects.get(pk=pk)
        query.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def index(request):
    return HttpResponse('polls')
