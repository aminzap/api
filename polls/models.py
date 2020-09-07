from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200, blank= True,null=True)
    pub_date = models.DateTimeField('published date', auto_now_add=True)
    question_update=models.DateTimeField('Update',auto_now=True)

    def __str__(self):
        return self.question_text


class Choise(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choise_text = models.CharField(max_length=200)
    vote = models.IntegerField(default=0)

    def __str__(self):
        return self.choise_text
