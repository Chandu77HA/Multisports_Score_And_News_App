from django.urls import path
from sportsquiz import views

urlpatterns = [

    path('general_knowledge_api/', views.general_knowledge_api, name = "general_knowledge_api"),
    path('all_sports_easy_api/', views.all_sports_easy_api, name = "all_sports_easy_api"),
    path('all_sports_medium_api/', views.all_sports_medium_api, name = "all_sports_medium_api"),
    path('all_sports_hard_api/', views.all_sports_hard_api, name = "all_sports_hard_api"),

    path('all_sports_api/', views.all_sports_api, name = "all_sports_api"),
    
]
