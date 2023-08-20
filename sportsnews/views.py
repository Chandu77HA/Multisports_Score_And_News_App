from django.shortcuts import render
import requests

# Create your views here.

# API KEY from https://newsapi.org/
API_KEY = '2541fb6e9afb4488b64cdca1c122a775'

# Function display sports news related to india
def india_sports_news(request):
    url = f"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey={API_KEY}"
    response = requests.get(url)
    data = response.json()
    articles = data['articles']
    context = {
        'title' : 'Latest Sports News Of India',
        'articles' : articles,
    }
    return render(request, 'sportsnews/sport_news.html', context)
