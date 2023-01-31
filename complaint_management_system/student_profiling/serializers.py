from rest_framework import serializers
from .models import UserModel
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework.exceptions import ValidationError




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id','username','matric_number','school','level','course_of_study', 'profile_picture','age','date_of_birth')
        extra_kwargs = {'read_only': ('id','matric_number')}