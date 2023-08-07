from authentication.models import User
from rest_framework import serializers

'''Serializer for Registration'''
class RegistrationSerializers(serializers.ModelSerializer):
    confirm_password = serializers.CharField(style ={'input_type': 'password'}, write_only = True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']
        extra_kwargs = {
            'password' : {'write_only' : True}
        }

    def save(self):

        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']

        # Check if password1 and confirm_password
        if password != confirm_password:
            raise serializers.ValidationError({'error': 'password and confirm_password should be same'})

        # Check if email already exist or not
        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'error': 'Eamil already exist'})
        
        account = User(email=self.validated_data['email'], username=self.validated_data['username'])
        account.set_password(password)
        account.save()

        return account



