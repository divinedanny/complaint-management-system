from .models import UserModel, StaffModel
from rest_framework import serializers
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from rest_framework.exceptions import ValidationError, AuthenticationFailed
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str,force_str,smart_bytes,DjangoUnicodeDecodeError,force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.hashers import make_password

# Create your serializers from here


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffModel
        fields = ('staff_number', 'department')
        extra_kwarge = {'matric_number':{'read_only':True},
        }

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id','username', 'email', 'first_name', 'last_name','profile_picture','date_of_birth','gender')
        extra_kwarge = {'id':{'read_only':True},
                        'email': {'required':True},
                        }
        
        


class RegisterUserSerializer(serializers.ModelSerializer):
    staff = StaffSerializer()
    confirm_password = serializers.CharField(max_length=128,)
    class Meta:
        model = UserModel
        fields = ('id','username', 'email', 'first_name', 'last_name', 'password','confirm_password','date_of_birth','gender','staff', 'profile_picture')
        extra_kwargs = {
                        'password':{'write_only': True,
                                    'required': True},
                        'confirm_password':{'write_only': True,
                                    'required': True},
                        'matric-number': {'write_only':True,
                                          'required': True},
                        'first_name': {'required': True},
                        'last_name': {'required': True},
                        'email': {'required': True},
                        'username': {'required': True},
                        }

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError(
            {"password": "Password fields didn't match."})
        return attrs
    
    
    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        staff = validated_data.pop('staff')
        user = UserModel.objects.create_user(
                                        username=validated_data['username'],
                                        email=validated_data['email'],
                                        password=validated_data['password'],
                                        first_name=validated_data['first_name'],
                                        last_name=validated_data['last_name'],
                                        date_of_birth=validated_data['date_of_birth'],
                                        gender=validated_data['gender'],
                                        profile_picture=validated_data['profile_picture'],
                                        )
        StaffModel.objects.create(staff=user, **staff)
        return user


class VerifyUserSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=555)
    class Meta:
        model = UserModel
        fields = ("token")
        
        
    
            
        

class LoginUserSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255, min_length=6)
    username = serializers.CharField(read_only=True, max_length=255)
    password = serializers.CharField(max_length=255, write_only=True)
    

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise ValidationError(_('Incorrect Credentials'))

        

class SetNewPasswordSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=555, min_length=1)
    password = serializers.CharField(max_length=255,min_length=6, write_only=True)
    confirm_password = serializers.CharField(max_length=255,min_length=6, write_only=True)
    uidb64 = serializers.CharField(min_length=1, write_only=True)
    class Meta:
        fields = ("token", 'password', 'confirm_password', 'uidb64')
        extra_kwargs = {
                        'password':{'write_only': True,
                                   'required': True},
                        'confirm_password':{'write_only': True,
                                   'required': True},
        }
    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError(
            {"password": "Password fields didn't match."})
        return attrs
    
    def  validate(self, attrs):
        try:
            password = attrs['password']
            uidb64 = attrs['uidb64']
            token = attrs['token']
            uid = smart_str(urlsafe_base64_decode(uidb64))
            user = UserModel.objects.get(pk=uid)
            if not PasswordResetTokenGenerator().check_token(user, token):
                return AuthenticationFailed('the reset link is invalid', 401)
            
            user.password = make_password(password)
            user.save()
        except Exception as e:
            return AuthenticationFailed('the reset link is invalid', 401)
        return super().validate(attrs)
        
        
class ForgotPasswordUserSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255, min_length=6)
    class Meta:
        fields = ('email',)
        
        
    def validate(self, attrs):
        email = attrs['data'].get('email')
        
        
        # else:
        #     raise serializers.ValidationError(
        #     {'email': 'Email does not exist'})
            
        return super().validate(attrs)