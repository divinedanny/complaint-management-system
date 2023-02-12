from cgitb import lookup
from lib2to3.pgen2 import token
from django.contrib.auth import login
from django.shortcuts import render,redirect
from .serializers import RegisterUserSerializer, UserSerializer, LoginUserSerializer
from rest_framework import generics, views, status
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
# Create your views here.

User = get_user_model()
# Login and registeration of users
class RegisterUserView(generics.CreateAPIView):
    serializer_class = RegisterUserSerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = (AllowAny, )
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                "user": UserSerializer(user, context=self.get_serializer_context()).data,
                "token": token.key
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class LoginUserView(generics.GenericAPIView):
    permission_classes = (AllowAny, )
    serializer_class = LoginUserSerializer
    parser_classes = [MultiPartParser, FormParser]

    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                "user": UserSerializer(user, context=self.get_serializer_context()).data,
                "token": token.key
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UpdateUserView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]
    lookup_field = 'pk'
    queryset = User.objects.all()

class UserListAllView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes= [SessionAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

# Update Profile, delete user,

class LogoutUserView(generics.DestroyAPIView):
    authentication_classes = [IsAuthenticated]
    lookup_field='pk'
    def post(self, request, *args, **kwargs):
        self.delete('pk')
        # request.user.auth_token.delete()