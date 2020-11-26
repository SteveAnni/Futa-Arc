from rest_framework import serializers
from .models import infoModel
class infoSerializer(serializers.ModelSerializer):
    class Meta:
        model = infoModel
        fields = '__all__'
