from django.shortcuts import render
from rest_framework import serializers, generics
from .models import ComplainsModel
from .serializers import ComplainsSerializers
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import authentication, permissions

# Create your views here.

class ComplainCreateView(generics.CreateAPIView):
    parser_classes= [MultiPartParser,FormParser]
    serializer_class = ComplainsSerializers
    authentication_classes= [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    
class ComplainEditView(generics.UpdateAPIView):
    lookup_field = 'pk'
    queryset = ComplainsModel.objects.all()
    parser_classes= [MultiPartParser,FormParser]
    serializer_class = ComplainsSerializers
    authentication_classes= [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
class ComplainListAllView(generics.ListAPIView):
    queryset = ComplainsModel.objects.all()
    serializer_class = ComplainsSerializers
    authentication_classes= [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
class ComplainDeleteView(generics.DestroyAPIView):
    lookup_field ='pk'
    queryset = ComplainsModel.objects.all()
    serializer_class= ComplainsSerializers
    authentication_classes= [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]