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

    path('l_matches/', views.l_matches, name = "l_matches"),
    path('rec_matches/', views.rec_matches, name = "rec_matches"),
    path('upcoming_matches/', views.upcoming_matches, name = "upcoming_matches"),

    path('recent_matches/', views.recent_matches, name = "recent_matches"),
    path('live_matches/', views.live_matches, name = "live_matches"),

    path('domestic/', views.domestic, name = "domestic"),

]

# http://127.0.0.1:8000/cricbuzz/cricbuzz_home/