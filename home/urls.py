from django.urls import path
from home import views

urlpatterns = [
    
    path('', views.home, name = 'home'),
    path('contact_us/', views.contact_us, name = 'contact_us'),
    path('about_us/', views.about_us, name = 'about_us'),

]