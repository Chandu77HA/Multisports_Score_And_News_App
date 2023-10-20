from django.urls import path, re_path
from cricbuzz import views

urlpatterns = [

    # URL for Cricbuzz Home and Layout
    path('cricbuzz_home/', views.cricbuzz_home, name = 'cricbuzz_home'),
    path('cricbuzz_layout/', views.cricbuzz_layout, name = 'cricbuzz_layout'),

    # Matches JSON urls
    path('l_matches/', views.l_matches, name = "l_matches"),
    path('rec_matches/', views.rec_matches, name = "rec_matches"),
    path('u_matches/', views.u_matches, name = "u_matches"),    

    # Matches HTML urls
    path('recent_matches/', views.recent_matches, name = "recent_matches"),
    path('live_matches/', views.live_matches, name = "live_matches"),
    path('upcoming_matches/', views.upcoming_matches, name = "upcoming_matches"),
    
    # Schedule HTML urls
    path('international_schedule/', views.international_schedule, name = 'international_schedule'),
    path('league_schedule/', views.league_schedule, name = 'league_schedule'),
    path('domestic_schedule/', views.domestic_schedule, name = 'domestic_schedule'),
    path('women_schedule/', views.women_schedule, name = "women_schedule"),

    path('schedule/<str:schedule_type>/', views.schedule_view, name='schedule'),

    path('api_player_list/', views.api_player_list, name = "api_player_list"),
    path('all_players_list/', views.all_players_list, name = "all_players_list"),
    path('display_players_data/', views.display_players_data, name = "display_players_data"),
    
]




# http://127.0.0.1:8000/cricbuzz/cricbuzz_home/

