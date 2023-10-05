from django.urls import path, re_path
from cricbuzz import views

urlpatterns = [

    path('international_schedule/', views.international_schedule, name = 'international_schedule'),
    path('league_schedule/', views.league_schedule, name = 'league_schedule'),
    path('domestic_schedule/', views.domestic_schedule, name = 'domestic_schedule'),

    path('schedule/<str:schedule_type>/', views.schedule_view, name='schedule'),
    
    path('cricbuzz_home/', views.cricbuzz_home, name = 'cricbuzz_home'),
    path('cric/', views.cric, name = 'cric'),
    path('check/', views.check, name = 'check'),

]

# http://127.0.0.1:8000/cricbuzz/cricbuzz_home/