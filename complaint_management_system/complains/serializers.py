from student.models import UserModel
from .models import ComplainsModel
from rest_framework import serializers


class ComplainsSerializers(serializers.ModelSerializer):
    class Meta:
        model = ComplainsModel
        fields = ['id','department','complain_message','complain_status','complain_upload','owner']
        extra_kwargs = {
            'owner': {'read_only': True},
            'complain_status': {'read_only': True},
        }
        
        def create(self, validated_data):
            user = UserModel.objects.get(id=validated_data)
            if validated_data['owner'] == user.email:
                validated_data['complain_status'] = 'INITIALIZED'
                return validated_data
            
            complaint = ComplainsModel.objects.create(
                complaint_status = validated_data['complaint_status'],
                complaint_message = validated_data['complaint_message'],
                department = validated_data['department'],
                complain_upload = validated_data['complaint_upload'],
                
            )
            return complaint