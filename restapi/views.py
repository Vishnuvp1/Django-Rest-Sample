from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from .models import Account
from rest_framework.permissions import IsAdminUser
from restapi.serializers import RegistrationSerializer, UsersSerializer

# Create your views here.

class RegisterAV(APIView):

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)

        data = {}

        if serializer.is_valid():
            account = serializer.save()
            
            data['response'] = "Registration successful!!"
            data['username'] = account.username
            data['email'] = account.email

            refresh = RefreshToken.for_user(account)

            data['token'] =  {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
        else:
            data = serializer.errors
            
        return Response(data)


class UsersAV(APIView):
    permission_classes = [IsAdminUser]
    def get(self, request):
        users = Account.objects.all()
        serializers = UsersSerializer(users, many=True)
        return Response(serializers.data)


class UserDetail(APIView):
    permission_classes = [IsAdminUser]
    def get(self, request, pk):
        try:
            user = Account.objects.get(pk=pk)
        except Account.DoesNotExist:
            return Response({'error' : 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        serializers = UsersSerializer(user)
        return Response(serializers.data)

    def put(self, request, pk):
        user = Account.objects.get(pk=pk)
        serializers = UsersSerializer(user, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = Account.objects.get(pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


