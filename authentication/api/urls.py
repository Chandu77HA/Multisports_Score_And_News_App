from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from authentication.api.views import registration_view, logut_view

urlpatterns = [

    # path('login/', obtain_auth_token, name = 'login'),
    # path('register/', registration_view, name = 'register'),
    # path('logout/', logut_view, name = 'logut'),

]

