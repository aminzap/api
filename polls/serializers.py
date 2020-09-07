from rest_framework import serializers
from . import models
class QuestionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Question
        fields='__all__'
class ChoiseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Choise
        fields='__all__'