from django.shortcuts import render
import requests
from sportsnews.models import SaveAllIndianSportsNews
from django.http import JsonResponse
from newsapi import NewsApiClient

# Create your views here.
# API KEY from https://newsapi.org/

API_KEY = '2541fb6e9afb4488b64cdca1c122a775'
newsapi = NewsApiClient(api_key='2541fb6e9afb4488b64cdca1c122a775')

# Function display sports news related to india and save all indian sports news
def india_sports_news(request):
    url = f"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey={API_KEY}"
    response = requests.get(url)
    data = response.json()
    articles = data['articles']
    if articles:
        for news in articles:
            news_title = news['title']
            check_news = SaveAllIndianSportsNews.objects.filter(title = news_title)
            if check_news.exists() or news_title == None:
                continue
            else:
                news_data = SaveAllIndianSportsNews(
                    title = news['title'],
                    source_name = news['source']['name'],
                    author = news['author'],
                    description = news['description'],
                    published_at = news['publishedAt'],
                    url = news['url'],
                    url_to_image = news['urlToImage'],
                    content = news['content'],
                )
                news_data.save()

        if request.method == 'GET':
            selected_news_title = request.GET.get('row.title')
            print(selected_news_title)
    context = {
        'title' : 'Latest Sports News Of India',
        'articles' : articles,
    }
    return render(request, 'sportsnews/india_sports_news.html', context)

# Function to get all news sources.
def all_news_sources(request):
    newsapi = NewsApiClient(api_key='2541fb6e9afb4488b64cdca1c122a775')
    sources = newsapi.get_sources()
    return JsonResponse(sources)

# Function to get all sports news sources.
def sports_sources(request):
    newsapi = NewsApiClient(api_key='2541fb6e9afb4488b64cdca1c122a775')
    sports_sources = newsapi.get_sources(category="sports", language="en")
    return JsonResponse(sports_sources)

# Function to get all sports top headlines.
def sports_top_headlines(request):
    top_headlines = newsapi.get_everything(sources='bleacher-report, espn, fox-sports',
                                            language='en',)
    articles = top_headlines['articles']
    context = {
        'title' : 'World Sports News',
        'articles' : articles,
    }
    return render(request, 'sportsnews/sports_news.html', context)

# Function to get all football top headlines.
def world_foofball_news(request):
    top_headlines = newsapi.get_everything(sources='four-four-two',language='en',)
    articles = top_headlines['articles']
    context = {
        'title' : 'World Football News',
        'articles' : articles,
    }
    return render(request, 'sportsnews/sports_news.html', context)

# Function to get all cricket top headlines.
def world_cricket_news(request):
    top_headlines = newsapi.get_everything(sources='espn-cric-info',language='en',)
    articles = top_headlines['articles']
    context = {
        'title' : 'World Cricket News',
        'articles' : articles,
    }
    return render(request, 'sportsnews/sports_news.html', context)

# Function to get all cricket top headlines.
def bbc_sports(request):
    top_headlines = newsapi.get_everything(sources='bbc-sport',language='en',)
    articles = top_headlines['articles']
    context = {
        'title' : 'World Cricket News',
        'articles' : articles,
    }
    return render(request, 'sportsnews/sports_news.html', context)