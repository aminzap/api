from django.contrib import admin
from . import models

@admin.register(models.Question)
class QuestionDisplay(admin.ModelAdmin):
    list_display = ['question_text', 'pub_date']
    search_fields = ['question_text']




@admin.register(models.Choise)
class ChoiseDisplay(admin.ModelAdmin):
    list_display = ['choise_text', 'vote']
    search_fields = ['choise_text']



