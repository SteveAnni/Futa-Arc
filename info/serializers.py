from rest_framework import serializers
from .models import infoModelClass
class infoSerializer(serializers.ModelSerializer):
    class Meta:
        model = infoModelClass
        fields = '__all__'
