from django.urls import path
from authentication import views

urlpatterns = [
    
    path('registration/', views.authregistration, name = 'registration'),
    path('login/', views.authlogin, name = 'login'),
    path('logout/', views.authlogout, name = 'logout'),
    path('profile/', views.profile, name = 'profile'),

    
]