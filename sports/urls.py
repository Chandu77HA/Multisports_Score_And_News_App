from django.urls import path
from sports import views

urlpatterns = [
    
    path('sports_detail/', views.sports_detail, name = 'sports_detail'),
    path('sports_info/<int:sport_id>/', views.sports_info, name = 'sports_info'),
    path('sports_form/', views.sports_form, name = 'sports_form'),

]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)