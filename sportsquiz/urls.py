from django.urls import path
from sportsquiz import views

urlpatterns = [

    path('sports_quiz_home/', views.sports_quiz_home, name="sports_quiz_home"),
    path('general_knowledge_api/', views.general_knowledge_api,
         name="general_knowledge_api"),
    path('all_sports_easy_api/', views.all_sports_easy_api,
         name="all_sports_easy_api"),
    path('all_sports_medium_api/', views.all_sports_medium_api,
         name="all_sports_medium_api"),
    path('all_sports_hard_api/', views.all_sports_hard_api,
         name="all_sports_hard_api"),

    path('all_sports_api/', views.all_sports_api, name="all_sports_api"),
    path('quiz_question_count/', views.quiz_question_count,
         name="quiz_question_count"),
    path('sports_quiz/<str:category_title>/',
         views.sports_quiz, name="sports_quiz"),

]
