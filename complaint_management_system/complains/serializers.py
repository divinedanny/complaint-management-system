from .models import ComplainsModel
from rest_framework import serializers


class ComplainsSerializers(serializers.ModelSerializer):
    class Meta:
        model = ComplainsModel
        fields = ['id','department','complain','level','course','school','matric_number','name','complain_upload']
        # read_only_fields = ('id')