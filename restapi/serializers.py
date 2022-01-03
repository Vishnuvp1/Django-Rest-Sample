from rest_framework import serializers
from . models import Account

class RegistrationSerializer(serializers.ModelSerializer):
    password2= serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = Account
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only' : True}
        }

    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'error': 'Passwords are not same!'})

        if Account.objects.filter(email=self.validated_data['email']).exists(): 
            raise serializers.ValidationError({'error': 'Email Already Exists!'})

        account = Account(email=self.validated_data['email'], username=self.validated_data['username'])
        account.set_password(password)
        account.save()

        return account

class UsersSerializer(serializers.ModelSerializer):
    password2= serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = Account
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only' : True}
        }

