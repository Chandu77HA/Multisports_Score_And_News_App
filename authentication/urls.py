from django.urls import path
from authentication import views

urlpatterns = [
    
    path('', views.home, name = 'home'),
    path('registration/', views.authregistration, name = 'registration'),
    path('login', views.authlogin, name = 'login'),
    path('logout/', views.authlogout, name = 'logout'),
    
]