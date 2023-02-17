import uuid
from .models import UserModel
from rest_framework import serializers
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from rest_framework.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        
        fields = ('id','username', 'matric_number', 'email', 'first_name', 'last_name', 'password','course_of_study','level','school','profile_picture','date_of_birth','gender')
        extra_kwarge = {'person_id':{'read_only':True},
                        'paswsword': {'write_only': True},
                        'email': {'required':True},
                        'age': {'read_only': True}
                        }
        


class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = UserModel
        fields = ['username','matric_number', 'email', 'first_name', 'last_name', 'password','course_of_study','level','school','date_of_birth','gender','profile_picture']
        extra_kwargs = {'password':{'write_only': True},
                        'matric-number': {'write_only':True,'required': True},
                        'first_name': {'required': True},
                        'last_name': {'required': True},
                        'email': {'required': True},}

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        user = UserModel.objects.create_user(username=validated_data['username'],
                                        email=validated_data['email'],
                                        password=validated_data['password'],
                                        first_name=validated_data['first_name'],
                                        last_name=validated_data['last_name'],
                                        matric_number=validated_data['matric_number'],
                                        course_of_study=validated_data['course_of_study'],
                                        level=validated_data['level'],
                                        school=validated_data['school'],
                                        date_of_birth=validated_data['date_of_birth'],
                                        gender=validated_data['gender'],
                                        profile_picture=validated_data['profile_picture'],
                                        )
        return user


class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise ValidationError(_('Incorrect Credentials'))

        
        
        
        