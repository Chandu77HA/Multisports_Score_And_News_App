"""
URL configuration for Multisports_Score_And_News project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    
    path('admin/', admin.site.urls),

    # App URLS
    path('', include('home.urls')),
    path('authentication/', include('authentication.urls')),
    path('sports/', include('sports.urls')),
    path('sportsnews/', include('sportsnews.urls')),
    path('cricbuzz/', include('cricbuzz.urls')),
    path('soccerhub/', include('soccerhub.urls')),
    path('sportsquiz/', include('sportsquiz.urls')),

    # App URLS for REST API
    path('api-authentication/', include('authentication.api.urls')),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
