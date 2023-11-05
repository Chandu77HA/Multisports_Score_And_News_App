from django.shortcuts import render
import requests
from django.http import JsonResponse
from cricbuzz.models import AllPlayersList, InternationalTeams
import time
from django.http import HttpResponse

# Create your views here.


def cricbuzz_home(request):
    return render(request, 'cricbuzz/cricbuzz_home.html')

def cricbuzz_layout(request):
    return render(request, 'cricbuzz/cricbuzz_layout.html')


def recent_matches(request):
    url = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/recent"
    headers = {
        "X-RapidAPI-Key": "746759c976mshc90186a6b287f40p144e07jsn86d0bada27a2",
        "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    match_json_data = response.json()
    recent_matches_data = match_json_data['typeMatches']
    match_data_recent = {
        'title' : 'Recent Matches',
        'match_schedule' : recent_matches_data,
    }
    return render(request, 'cricbuzz/recent_matches.html', context = match_data_recent)

# To check JSON data
def rec_matches(request):
    url = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/recent"

    headers = {
        "X-RapidAPI-Key": "746759c976mshc90186a6b287f40p144e07jsn86d0bada27a2",
        "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    data = response.json()
    return JsonResponse(data)


def live_matches(request):
    url = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/live"
    headers = {
        "X-RapidAPI-Key": "746759c976mshc90186a6b287f40p144e07jsn86d0bada27a2",
        "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    match_json_data = response.json()
    live_matches_data = match_json_data['typeMatches']
    match_data_live = {
        'title' : 'Live Matches',
        'match_schedule' : live_matches_data,
    }
    return render(request, 'cricbuzz/live_matches.html', context = match_data_live)

# To check JSON data
def l_matches(request):
    url = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/live"

    headers = {
        "X-RapidAPI-Key": "746759c976mshc90186a6b287f40p144e07jsn86d0bada27a2",
        "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    data = response.json()
    return JsonResponse(data)


def upcoming_matches(request):
    url = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/upcoming"

    headers = {
        "X-RapidAPI-Key": "746759c976mshc90186a6b287f40p144e07jsn86d0bada27a2",
        "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    match_json_data = response.json()
    upcoming_matches_data = match_json_data['typeMatches']
    match_data_live = {
        'title' : 'Upcoming Matches',
        'match_schedule' : upcoming_matches_data,
    }
    return render(request, 'cricbuzz/upcoming_matches.html', context = match_data_live)


# To check JSON data
def u_matches(request):
    url = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/upcoming"

    headers = {
        "X-RapidAPI-Key": "746759c976mshc90186a6b287f40p144e07jsn86d0bada27a2",
        "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    data = response.json()
    return JsonResponse(data)


def international_schedule(request):
    url = "https://cricbuzz-cricket.p.rapidapi.com/schedule/v1/international"
    headers = {
        "X-RapidAPI-Key": "746759c976mshc90186a6b287f40p144e07jsn86d0bada27a2",
        "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    json_data = response.json()
    international_schedule_data = json_data['matchScheduleMap']
    context = {
        'title' : 'Schedule of International matches',
        'match_schedule' : international_schedule_data,
    }
    return render(request, 'cricbuzz/match_schedule.html', context)

def league_schedule(request):
    url = "https://cricbuzz-cricket.p.rapidapi.com/schedule/v1/league"

    headers = {
        "X-RapidAPI-Key": "746759c976mshc90186a6b287f40p144e07jsn86d0bada27a2",
        "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    json_data = response.json()
    league_schedule_data = json_data['matchScheduleMap']
    context = {
        'title' : 'Schedule of League matches',
        'match_schedule' : league_schedule_data,
    }
    return render(request, 'cricbuzz/match_schedule.html', context)

def domestic_schedule(request):
    url = "https://cricbuzz-cricket.p.rapidapi.com/schedule/v1/domestic"

    headers = {
        "X-RapidAPI-Key": "746759c976mshc90186a6b287f40p144e07jsn86d0bada27a2",
        "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    json_data = response.json()
    domestic_schedule_data = json_data['matchScheduleMap']
    context = {
        'title' : 'Schedule of Domestic matches',
        'match_schedule' : domestic_schedule_data,
    }
    return render(request, 'cricbuzz/match_schedule.html', context)

def women_schedule(request):
    url = "https://cricbuzz-cricket.p.rapidapi.com/schedule/v1/women"

    headers = {
        "X-RapidAPI-Key": "746759c976mshc90186a6b287f40p144e07jsn86d0bada27a2",
        "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    match_json_data = response.json()
    women_matches_data = match_json_data['matchScheduleMap']
    match_data_live = {
        'title' : 'Women Matches',
        'match_schedule' : women_matches_data,
    }
    return render(request, 'cricbuzz/match_schedule.html', context = match_data_live)


def schedule_view(request, schedule_type):
    url = f"https://cricbuzz-cricket.p.rapidapi.com/schedule/v1/{schedule_type}"

    headers = {
        "X-RapidAPI-Key": "746759c976mshc90186a6b287f40p144e07jsn86d0bada27a2",
        "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    print(response)
    json_data = response.json()
    schedule_data = json_data['matchScheduleMap']
    context = {
        'title': f'Schedule of {schedule_type.capitalize()} matches',
        'match_schedule': schedule_data,
    }
    return render(request, 'cricbuzz/match_schedule.html', context)


def api_player_list(request):
    url = "https://cricbuzz-cricket.p.rapidapi.com/stats/v1/player/search"
    querystring = {"plrN":""}
    headers = {
        "X-RapidAPI-Key": "746759c976mshc90186a6b287f40p144e07jsn86d0bada27a2",
        "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    player_data = data['player']
    return JsonResponse(data)


def all_players_list(request):
    url = "https://cricbuzz-cricket.p.rapidapi.com/stats/v1/player/search"
    querystring = {"plrN": ""}
    headers = {
        "X-RapidAPI-Key": "746759c976mshc90186a6b287f40p144e07jsn86d0bada27a2",
        "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    player_json_data = data['player']
    print(type(data))
    print(type(player_json_data))
    print(type(data.get("player", [])))
    # print(data.get("player", []))

    # Iterate through player data and save if it doesn't already exist
    for player_data in data.get("player", []):
        cricbuzz_id = int(player_data.get("id"))
        
        # Check if a player with the same cricbuzz_id already exists
        if not AllPlayersList.objects.filter(cricbuzz_id=cricbuzz_id).exists():
            player_name = player_data.get("name")
            team_name = player_data.get("teamName")
            face_image_id = int(player_data.get("faceImageId"))
            
            # Create and save a new instance of the model
            AllPlayersList.objects.create(
                cricbuzz_id=cricbuzz_id,
                player_name=player_name,
                team_name=team_name,
                face_image_id=face_image_id
            )
    
    players = AllPlayersList.objects.all()
    context = {
        'title' : 'All Players List',
        'players': players,
    }
    return render(request, 'cricbuzz/all_players_list.html', context)



'''
Code refactoring is defined as the process of restructuring computer code without changing 
or adding to its external behavior and functionality.

'''

# Refractoring above function and split it in to three functions that do seperate functionality.

def get_players_cricbuzz_data():
    url = "https://cricbuzz-cricket.p.rapidapi.com/stats/v1/player/search"
    querystring = {"plrN": ""}
    headers = {
        "X-RapidAPI-Key": "746759c976mshc90186a6b287f40p144e07jsn86d0bada27a2",
        "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    player_json_data = data['player']
    return player_json_data

def save_player(player_data):
    cricbuzz_id = int(player_data['id'])
    if not AllPlayersList.objects.filter(cricbuzz_id=cricbuzz_id).exists():
        player_name = player_data['name']
        team_name = player_data['teamName']
        face_image_id = player_data['faceImageId']
        AllPlayersList.objects.create(
            cricbuzz_id=cricbuzz_id,
            player_name=player_name,
            team_name=team_name,
            face_image_id=face_image_id
        )


def display_players_data(request):
    start_time = time.time()

    # '''
    player_data = get_players_cricbuzz_data()
    for player in player_data:
        save_player(player)
    # '''

    # Uncomment the above three line to go through cricbuzz players api and save all recently updated players in model AllPlayersList
    # Comment the above three line to reduce the url runtime
    # It will just display all the players data that is already stored in django model (name - AllPlayersList)
    # Instead of going through cricbuzz players api

    players = AllPlayersList.objects.all()
    end_time = time.time()
    execution_time = end_time - start_time
    print(execution_time)
    context = {
        'title': 'All Players List',
        'players': players,
    }
    return render(request, 'cricbuzz/display_players_data.html', context)


def player_info_api(request):
    url = "https://cricbuzz-cricket.p.rapidapi.com/stats/v1/player/587"
    headers = {
        "X-RapidAPI-Key": "746759c976mshc90186a6b287f40p144e07jsn86d0bada27a2",
        "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    return JsonResponse(data)


def player_info(request):
    if request.method == 'POST':
        search_query = request.POST.get('search_query')
        if search_query:
            search_query = search_query.lower()
            try:
                check_player = AllPlayersList.objects.get(player_name__iexact=search_query)
                if check_player is not None:
                    cricbuzz_id = check_player.cricbuzz_id
                    request.session['cricbuzz_id'] = cricbuzz_id
                    url = f"https://cricbuzz-cricket.p.rapidapi.com/stats/v1/player/{cricbuzz_id}"
                    headers = {
                        "X-RapidAPI-Key": "746759c976mshc90186a6b287f40p144e07jsn86d0bada27a2",
                        "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
                    }
                    response = requests.get(url, headers=headers)
                    
                    if response.status_code == 200:
                        player_info_data = response.json()
                        context = {
                            'title': 'Player Information',
                            'player_info': player_info_data,
                        }
                        return render(request, 'cricbuzz/player_info.html', context)
                    else:
                        return HttpResponse("Error fetching player data from the API")
                else:
                    return HttpResponse("Player not found")
            except AllPlayersList.DoesNotExist:
                return HttpResponse("Player not found")
        else:
            return HttpResponse("Please enter a player's name")
    else:
        # Handle the case when the request method is not 'POST'
        cricbuzz_id = request.session.get('cricbuzz_id')
        url = f"https://cricbuzz-cricket.p.rapidapi.com/stats/v1/player/{cricbuzz_id}"
        headers = {
            "X-RapidAPI-Key": "746759c976mshc90186a6b287f40p144e07jsn86d0bada27a2",
            "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers)
        player_info_data = response.json()
        context = {
            'title': 'Player Information',
            'player_info': player_info_data,
        }
        return render(request, 'cricbuzz/player_info.html', context)


def check_player(request):
    return render(request, 'cricbuzz/check_player.html')


def player_batting_api(request):
    url = "https://cricbuzz-cricket.p.rapidapi.com/stats/v1/player/1413/batting"
    headers = {
        "X-RapidAPI-Key": "746759c976mshc90186a6b287f40p144e07jsn86d0bada27a2",
        "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    return JsonResponse(data)


def player_batting(request):
    cricbuzz_id = request.session.get('cricbuzz_id')
    if cricbuzz_id:
        url = f"https://cricbuzz-cricket.p.rapidapi.com/stats/v1/player/{cricbuzz_id}/batting"
        headers = {
            "X-RapidAPI-Key": "746759c976mshc90186a6b287f40p144e07jsn86d0bada27a2",
            "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers)
        player_batting_data = response.json()
        context = {
            'title': 'Player Batting',
            'player_batting_data': player_batting_data,
        }
        return render(request, 'cricbuzz/player_batting.html', context)
    else:
        return HttpResponse("Cricbuzz ID not found in the session")


def player_bowling_api(request):
    url = "https://cricbuzz-cricket.p.rapidapi.com/stats/v1/player/1413/bowling"
    headers = {
        "X-RapidAPI-Key": "746759c976mshc90186a6b287f40p144e07jsn86d0bada27a2",
        "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    return JsonResponse(data)

def player_bowling(request):
    cricbuzz_id = request.session.get('cricbuzz_id')
    if cricbuzz_id:
        url = f"https://cricbuzz-cricket.p.rapidapi.com/stats/v1/player/{cricbuzz_id}/bowling"
        headers = {
            "X-RapidAPI-Key": "746759c976mshc90186a6b287f40p144e07jsn86d0bada27a2",
            "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers)
        player_bowling_data = response.json()
        context = {
            'title': 'Player Bowling',
            'player_bowling_data': player_bowling_data,
        }
        return render(request, 'cricbuzz/player_bowling.html', context)
    else:
        return HttpResponse("Cricbuzz ID not found in the session")

def player_news_api(request):
    url = "https://cricbuzz-cricket.p.rapidapi.com/news/v1/player/1413"
    headers = {
        "X-RapidAPI-Key": "746759c976mshc90186a6b287f40p144e07jsn86d0bada27a2",
        "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    return JsonResponse(data)


def player_news(request):
    cricbuzz_id = request.session.get('cricbuzz_id')
    if cricbuzz_id:
        url = f"https://cricbuzz-cricket.p.rapidapi.com/news/v1/player/{cricbuzz_id}"
        headers = {
            "X-RapidAPI-Key": "746759c976mshc90186a6b287f40p144e07jsn86d0bada27a2",
            "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers)
        player_news_data = response.json()
        context = {
            'title': 'Player Career',
            'player_news_data': player_news_data,
        }
        return render(request, 'cricbuzz/player_news.html', context)
    else:
        return HttpResponse("Cricbuzz ID not found in the session")


def player_career_api(request):
    url = "https://cricbuzz-cricket.p.rapidapi.com/stats/v1/player/1413/career"
    headers = {
        "X-RapidAPI-Key": "746759c976mshc90186a6b287f40p144e07jsn86d0bada27a2",
        "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    return JsonResponse(data)

def player_career(request):
    cricbuzz_id = request.session.get('cricbuzz_id')
    if cricbuzz_id:
        url = f"https://cricbuzz-cricket.p.rapidapi.com/stats/v1/player/{cricbuzz_id}/career"
        headers = {
            "X-RapidAPI-Key": "746759c976mshc90186a6b287f40p144e07jsn86d0bada27a2",
            "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers)
        player_career_data = response.json()
        context = {
            'title': 'Player Career',
            'player_career_data': player_career_data,
        }
        return render(request, 'cricbuzz/player_career.html', context)
    else:
        return HttpResponse("Cricbuzz ID not found in the session")

# Teams
def team_list_international_api(request):
    url = "https://cricbuzz-cricket.p.rapidapi.com/teams/v1/international"
    headers = {
        "X-RapidAPI-Key": "746759c976mshc90186a6b287f40p144e07jsn86d0bada27a2",
        "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    return JsonResponse(data)


def team_list_international(request):
    url = "https://cricbuzz-cricket.p.rapidapi.com/teams/v1/international"
    headers = {
        "X-RapidAPI-Key": "746759c976mshc90186a6b287f40p144e07jsn86d0bada27a2",
        "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    international_team_data = data['list']
    the_team_type = None
    team_type = None
    for international_team in international_team_data:
        if len(international_team) <= 2:
            the_team_type = international_team['teamName']
            if the_team_type == "Test Teams":
                team_type = "Test Team"
            elif the_team_type == "Associate Teams":
                team_type = "Associate Team"
            continue
        else:
            cricbuzz_team_id = international_team['teamId']
            team_name = international_team['teamName']
            team_sub_name = international_team['teamSName']
            image_id = international_team['imageId']
            try:
                country_name = international_team['countryName']
            except KeyError:
                country_name = None
            if not InternationalTeams.objects.filter(cricbuzz_team_id=cricbuzz_team_id).exists():
                InternationalTeams.objects.create(
                    cricbuzz_team_id=cricbuzz_team_id,
                    team_name=team_name,
                    team_sub_name=team_sub_name,
                    image_id=image_id,
                    country_name=country_name,
                    team_type=team_type
                    )
    international_teams = InternationalTeams.objects.all()
    context = {
            'title': 'International Teams',
            'international_teams': international_teams,
        }
    return render(request, 'cricbuzz/Teams/international_teams.html', context)


def team_list_league_api(request):
    url = "https://cricbuzz-cricket.p.rapidapi.com/teams/v1/league"
    headers = {
        "X-RapidAPI-Key": "746759c976mshc90186a6b287f40p144e07jsn86d0bada27a2",
        "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    return JsonResponse(data)


def team_list_domestic_api(request):
    url = "https://cricbuzz-cricket.p.rapidapi.com/teams/v1/domestic"
    headers = {
        "X-RapidAPI-Key": "746759c976mshc90186a6b287f40p144e07jsn86d0bada27a2",
        "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    return JsonResponse(data)

def team_list_women_api(request):
    url = "https://cricbuzz-cricket.p.rapidapi.com/teams/v1/women"
    headers = {
        "X-RapidAPI-Key": "746759c976mshc90186a6b287f40p144e07jsn86d0bada27a2",
        "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    return JsonResponse(data)


def team_schedules_api(request):
    url = "https://cricbuzz-cricket.p.rapidapi.com/teams/v1/2/schedule"
    headers = {
        "X-RapidAPI-Key": "746759c976mshc90186a6b287f40p144e07jsn86d0bada27a2",
        "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    return JsonResponse(data)

def team_results_api(request):
    url = "https://cricbuzz-cricket.p.rapidapi.com/teams/v1/2/results"
    headers = {
        "X-RapidAPI-Key": "746759c976mshc90186a6b287f40p144e07jsn86d0bada27a2",
        "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    return JsonResponse(data)

def team_news_api(request):
    url = "https://cricbuzz-cricket.p.rapidapi.com/news/v1/team/2"
    headers = {
        "X-RapidAPI-Key": "746759c976mshc90186a6b287f40p144e07jsn86d0bada27a2",
        "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    return JsonResponse(data)

def team_players_api(request):
    url = "https://cricbuzz-cricket.p.rapidapi.com/teams/v1/2/players"
    headers = {
        "X-RapidAPI-Key": "746759c976mshc90186a6b287f40p144e07jsn86d0bada27a2",
        "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    return JsonResponse(data)

def team_stats_filters_api(request):
    url = "https://cricbuzz-cricket.p.rapidapi.com/stats/v1/team/2"
    headers = {
        "X-RapidAPI-Key": "746759c976mshc90186a6b287f40p144e07jsn86d0bada27a2",
        "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    return JsonResponse(data)

def team_stats_api(request):
    url = "https://cricbuzz-cricket.p.rapidapi.com/stats/v1/team/2"
    querystring = {"statsType":"mostRuns"}
    headers = {
        "X-RapidAPI-Key": "746759c976mshc90186a6b287f40p144e07jsn86d0bada27a2",
        "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    return JsonResponse(data)


# Photos
def photos_list_api(request):
    url = "https://cricbuzz-cricket.p.rapidapi.com/photos/v1/index"
    headers = {
        "X-RapidAPI-Key": "746759c976mshc90186a6b287f40p144e07jsn86d0bada27a2",
        "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    return JsonResponse(data)


def photos_get_gallery_api(request):
    url = "https://cricbuzz-cricket.p.rapidapi.com/photos/v1/detail/5754"
    headers = {
        "X-RapidAPI-Key": "746759c976mshc90186a6b287f40p144e07jsn86d0bada27a2",
        "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    return JsonResponse(data)


def get_image_api(request):
    url = "https://cricbuzz-cricket.p.rapidapi.com/img/v1/i1/c2318/i.jpg"
    headers = {
        "X-RapidAPI-Key": "746759c976mshc90186a6b287f40p144e07jsn86d0bada27a2",
        "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    return JsonResponse(response)
