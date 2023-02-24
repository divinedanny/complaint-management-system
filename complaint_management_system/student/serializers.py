from asyncore import read
from dataclasses import fields
from lib2to3.pgen2 import token
import uuid
from .models import UserModel, StudentModel
from rest_framework import serializers
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from rest_framework.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Create your serializers from here


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        fields = ('matric_number','course_of_study','level','school')
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
    student = StudentSerializer()
    confirm_password = serializers.CharField(max_length=128,)
    class Meta:
        model = UserModel
        fields = ('id','username', 'email', 'first_name', 'last_name', 'password','confirm_password','date_of_birth','gender','student')
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
        student = validated_data.pop('student')
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
        StudentModel.objects.create(student=user, **student)
        return user


class VerifyUserSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=555)
    class Meta:
        model = UserModel
        fields = ("token")
        
        
    
            
        

class LoginUserSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255, min_length=6)
    username = serializers.CharField(read_only=True, max_length=255)
    password = serializers.CharField(max_length=255, write_only=True)
    

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise ValidationError(_('Incorrect Credentials'))

        
        
        
        
        
        
        
