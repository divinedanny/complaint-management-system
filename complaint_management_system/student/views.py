from django.contrib.sites.shortcuts import get_current_site
from rest_framework_simplejwt.tokens import RefreshToken
from django.urls import reverse
from .models import UserModel
from .serializers import RegisterUserSerializer, UserSerializer, LoginUserSerializer, VerifyUserSerializer
from rest_framework import generics, status, views
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from .utils import Util
import jwt
from django.conf import settings
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Create your views here.

User = get_user_model()
# Login and registeration of users
class RegisterUserView(generics.CreateAPIView):
    serializer_class = RegisterUserSerializer
    parser_classes = (FormParser, MultiPartParser)
    permission_classes = (AllowAny, )
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            
            #   sending verification link to user
            email_token = RefreshToken.for_user(user).access_token
            subject='Welcome to your complaint management system'
            current_site = get_current_site(request).domain
            relativeurl = reverse('verify-user') 
            absoluteurl = 'http://'+current_site+relativeurl+'?token='+str(email_token)
            message=f"""HI,{user.username},\n
            Welcome to your complaint management system.\n
            please use the link below to verify yout email address.\n
            {absoluteurl}
            \n
            If you did not request this, please ignore this email.
            \n 
            Thanks for registering.
            """
            receiver_email = (user.email,)
            data = {"message": message, 'subject': subject, 'to': receiver_email,}
            print(data)
            Util.send_email(data)
            return Response({
                "user": UserSerializer(user, context=self.get_serializer_context()).data,
                "token": token.key
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def generate_verification_pin():
    # rand_gen = randint(1000,9999)
    rand_gen = 1123
    print(rand_gen)
    return rand_gen
    
class LoginUserView(generics.GenericAPIView):
    permission_classes = (AllowAny, )
    serializer_class = LoginUserSerializer
    parser_classes = (FormParser,MultiPartParser)

    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                "token": token.key
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
class VerifyUserView(views.APIView):
    serializer_class = VerifyUserSerializer
    token_param_config=openapi.Parameter('token', in_=openapi.IN_QUERY, type=openapi.TYPE_STRING)
    
    
    
    @swagger_auto_schema(manual_parameters=[token_param_config])
    def get(self, request, *args, **kwargs):
        token = request.GET.get('token')
        
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            user = User.objects.get(id=payload['user_id'])
            if not user.is_verified:
                user.is_verified = True
                user.save()
            return Response({
                "email": "User is verified and Successfully Activated!!"
            }, status=status.HTTP_200_OK)
        
        except jwt.ExpiredSignatureError as expired:
            return Response({"error":"activation link is expired."}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.InvalidTokenError as invalid:
            return Response({"error":"activation link is invalid."}, status=status.HTTP_400_BAD_REQUEST)
        
        

class UpdateUserView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]
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
    serializer_class = UserSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field='pk'
    def post(self, request, *args, **kwargs):
        self.delete('pk')
        # request.user.auth_token.delete()
        
        
        
        
        
