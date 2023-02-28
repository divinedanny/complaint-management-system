from django.shortcuts import render
from rest_framework import serializers, generics, status
from .models import ComplainsModel
from .serializers import ComplainsSerializers, RegisterComplainsSerializers
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

# Create your views here.

class ComplainCreateView(generics.CreateAPIView):
    queryset = ComplainsModel.objects.all()
    parser_classes= [MultiPartParser,FormParser]
    serializer_class = RegisterComplainsSerializers
    authentication_classes= [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save(owner=self.request.user)

            return Response({
                    "user": ComplainsSerializers(user, context=self.get_serializer_context()).data,
                }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        

    
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