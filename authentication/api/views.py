from rest_framework.decorators import api_view
from authentication.api.serializers import RegistrationSerializers
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status


'''Function For User Registration and generate Token'''
@api_view(['POST',])
def registration_view(request):

    if request.method == 'POST':
        serializer = RegistrationSerializers(data = request.data)

        registration_data = {}

        if serializer.is_valid():
            account = serializer.save()

            registration_data['response'] = "Registration Successful!"
            registration_data['username'] = account.username
            registration_data['email'] = account.email

            token = Token.objects.get(user=account).key
            registration_data['token'] = token

        else:
            registration_data = serializer.errors

        return Response(registration_data)
    

'''Function for Logut using Token'''
@api_view(['POST',])
def logut_view(request):

    logout_data = {}
    
    if request.method == 'POST':
        logout_data['user'] = str(request.user)
        request.user.auth_token.delete()
        logout_data['response'] = 'Logout Successful!'
        
        return Response(logout_data, status = status.HTTP_200_OK)
