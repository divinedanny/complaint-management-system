from django.contrib.sites.shortcuts import get_current_site
from rest_framework_simplejwt.tokens import RefreshToken
from django.urls import reverse
from .models import UserModel
from .serializers import RegisterUserSerializer, UserSerializer, LoginUserSerializer, VerifyUserSerializer, ForgotPasswordUserSerializer, SetNewPasswordSerializer
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
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str,force_str,smart_bytes,DjangoUnicodeDecodeError,force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

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
            please use the link below to verify your email address.\n
            {absoluteurl}\n
            If you did not request this, please ignore this email.        \n Thanks for registering.
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
    permission_classes = (AllowAny, )
    serializer_class = VerifyUserSerializer
    token_param_config=openapi.Parameter('token', in_=openapi.IN_QUERY, description='Description',type=openapi.TYPE_STRING)
    
    @swagger_auto_schema(manual_parameters=[token_param_config])
    def get(self, request):
        token = request.GET.get('token')
        try:
            payload = jwt.decode(token, settings.SECRET_KEY)
            user = UserModel.objects.get(id=payload['user_id'])
            if not user.is_verified and not user.is_staff:
                user.is_verified = True
                user.is_staff = True
                user.save()
            return Response({"email": "User is verified and Successfully Activated!!"}, status=status.HTTP_200_OK)
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
    queryset = UserModel.objects.all()
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
        
        
class ForgotPasswordView(generics.GenericAPIView):
    serializer_class = ForgotPasswordUserSerializer
    permission_classes = (AllowAny, )
    
    def post(self, request, *args, **kwargs):
        data = {"request": request, 'data': request.data}
        serializer = self.serializer_class(data=request.data)
        email = request.data['email']
        if UserModel.objects.filter(email=email).exists():
            user = UserModel.objects.get(email=email)
            uuid_bytes = force_bytes(user.id)
            uidb64 = urlsafe_base64_encode(uuid_bytes)
            token = PasswordResetTokenGenerator().make_token(user)
            current_site = get_current_site(request = request).domain
            relativeurl = reverse('password-reset-confirmed', kwargs={'uidb64': uidb64,'token': token}) 
            absoluteurl = 'http://'+current_site+relativeurl
            message=f"""
            please use the link below to reset your password.\n
            {absoluteurl}
            \n
            If you did not request this, please ignore this email.
            
            """
            subject='Reset your password'
            receiver_email = (user.email,)
            data = {"message": message, 'subject': subject, 'to': receiver_email,}
            print(data)
            Util.send_email(data)
        return Response({'success': 'Your reset password link has been sent'}, status=status.HTTP_200_OK)
        
        
        
class PasswordResetView(generics.GenericAPIView):
    serializer_class = ForgotPasswordUserSerializer
    
    def get(self, request, uidb64,token):
        try:
            uid = smart_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
            if not PasswordResetTokenGenerator().check_token(user, token):
                return Response({'failure': 'invalid token'}, status=status.HTTP_400_BAD_REQUEST)
            
            # return HttpResponseRedirect(redirect_to=f'{reverse("password-reset-complete")}', {'success': True, 'message': 'Credentials are Valid','uidb64': uidb64, 'token': token}, status=status.HTTP_200_OK)
            return Response({'success': True, 'message': 'Credentials are Valid','uidb64': uidb64, 'token': token}, status=status.HTTP_200_OK, headers={'Location': reverse('password-reset-complete')})
            # return redirect('password-reset-complete
            
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
            return Response({'failure': 'user does not exist'}, status=status.HTTP_404_NOT_FOUND)
            
class SetNewPasswordView(generics.GenericAPIView): 
    serializer_class = SetNewPasswordSerializer  
    def patch(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'success': True, 'message': 'password request is successfully changed'}, status=status.HTTP_200_OK)
        
        