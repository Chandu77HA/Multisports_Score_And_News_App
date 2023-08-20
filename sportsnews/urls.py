from django.urls import path
from sportsnews import views

urlpatterns = [

    path('india_sports_news/', views.india_sports_news, name = 'india_sports_news'),

]
