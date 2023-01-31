from urllib import response
from django.shortcuts import render,redirect
from .serializers import RegisterUserSerializer, UserSerializer, LoginSerializer
from rest_framework import generics, views, status
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
# Create your views here.

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

    
class LoginUserView(views.APIView):
    permission_classes = (AllowAny, )
    serializer_class = LoginSerializer
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

        # serializer.is_valid(raise_exception=True)
        # user = serializer.validated_data['user']
        # login(request, user)
        # return user


# Update Profile, delete user,