from django.urls import path
from . import views
urlpatterns = [
    # path('', views.index),
    path('get-question-obj/',views.GetQuestionData.as_view()),
    path('see-data/',views.searchDef),
    path('get-choise-obj/',views.GetChoiseData.as_view()),
    path('update-question/<int:pk>/',views.UpdateQuestion.as_view()),
    path('post-data/',views.PostData.as_view()),
    path('search/',views.Search.as_view()),
    path('delete/<int:pk>/',views.DeleteData.as_view()),
]