from django.urls import path
from sports import views

urlpatterns = [
    
    path('sports_detail/', views.sports_detail, name = 'sports_detail'),
    path('sports_info/<int:sport_id>/', views.sports_info, name = 'sports_info'),
    path('sports_form/', views.sports_form, name = 'sports_form'),
    path('delete_sport/<int:sport_id>/', views.delete_sport, name = 'delete_sport'),
    path('edit_sport/<int:sport_id>/', views.edit_sport, name = 'edit_sport'),

]
