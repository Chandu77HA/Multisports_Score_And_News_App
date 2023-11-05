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

    # Player data HTML urls
    path('api_player_list/', views.api_player_list, name = "api_player_list"),
    path('all_players_list/', views.all_players_list, name = "all_players_list"),
    path('display_players_data/', views.display_players_data, name = "display_players_data"),
    path('player_info/', views.player_info, name = "player_info"),
    path('player_batting/', views.player_batting, name = "player_batting"),
    path('player_bowling/', views.player_bowling, name = "player_bowling"),
    path('player_career/', views.player_career, name = "player_career"),
    path('player_news/', views.player_news, name = "player_news"),

    path('check_player/', views.check_player, name = "check_player"),

    # Player data JSON urls
    path('player_info_api/', views.player_info_api, name = "player_info_api"),
    path('player_batting_api/', views.player_batting_api, name = "player_batting_api"),
    path('player_bowling_api/', views.player_bowling_api, name = "player_bowling_api"),
    path('player_news_api/', views.player_news_api, name = "player_news_api"),
    path('player_career_api/', views.player_career_api, name = "player_career_api"),

    # Teams data JSON urls
    path('team_list_international_api/', views.team_list_international_api, name = "team_list_international_api"),
    path('team_list_league_api/', views.team_list_league_api, name = "team_list_league_api"),
    path('team_list_league_api/', views.team_list_league_api, name = "team_list_league_api"),
    path('team_list_women_api/', views.team_list_women_api, name = "team_list_women_api"),
    path('team_schedules_api/', views.team_schedules_api, name = "team_schedules_api"),
    path('team_results_api/', views.team_results_api, name = "team_results_api"),
    path('team_news_api/', views.team_news_api, name = "team_news_api"),
    path('team_players_api/', views.team_players_api, name = "team_players_api"),
    path('team_stats_filters_api/', views.team_stats_filters_api, name = "team_stats_filters_api"),
    path('team_stats_api/', views.team_stats_api, name = "team_stats_api"),

    # Teams data HTML urls

    path('team_list_international/', views.team_list_international, name = "team_list_international"),

    # Photos data JSON urls
    path('photos_list_api/', views.photos_list_api, name = "photos_list_api"),
    path('photos_get_gallery_api/', views.photos_get_gallery_api, name = "photos_get_gallery_api"),
    path('get_image_api/', views.get_image_api, name = "teget_image_apiam_stats"),
    
]


