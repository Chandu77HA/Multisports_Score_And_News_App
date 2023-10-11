from django.shortcuts import render
import requests
from django.http import JsonResponse

# Create your views here.


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
    return render(request, 'cricbuzz/recent_matches.html', context = match_data_live)


def rec_matches(request):
    url = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/recent"

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

def cric(request):
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
    return render(request, 'cricbuzz/cric.html', context)

def cricbuzz_home(request):
    return render(request, 'cricbuzz/check_home.html')

def cricbuzz_layout(request):
    return render(request, 'cricbuzz/cricbuzz_layout.html')

def check(request):
    return render(request, 'cricbuzz/check.html')

def domestic(request):
    url = "https://cricbuzz-cricket.p.rapidapi.com/schedule/v1/domestic"

    headers = {
        "X-RapidAPI-Key": "746759c976mshc90186a6b287f40p144e07jsn86d0bada27a2",
        "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    return JsonResponse(data)

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
    data = response.json()
    return JsonResponse(data)
