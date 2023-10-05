from django.urls import path
from sportsnews import views

urlpatterns = [

    path('india_sports_news/', views.india_sports_news, name = 'india_sports_news'),

    path('all_news_sources/', views.all_news_sources, name = 'all_news_sources'),
    path('sports_sources/', views.sports_sources, name = 'sports_sources'),
    
    path('sports_top_headlines/', views.sports_top_headlines, name = 'sports_top_headlines'),
    path('world_foofball_news/', views.world_foofball_news, name = 'world_foofball_news'),
    path('world_cricket_news/', views.world_cricket_news, name = 'world_cricket_news'),
    path('bbc_sports/', views.bbc_sports, name = 'bbc_sports'),


]


