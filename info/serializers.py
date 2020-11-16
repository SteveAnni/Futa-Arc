from rest_framework import serializers
from .models import infoModel, aggregateList
class infoSerializer(serializers.ModelSerializer):
    class Meta:
        model = infoModel
        fields = '__all__'


class aggregateListSerializer(serializers.ModelSerializer):

    def save(self):
        aggregateList.objects.update_or_create(username=self.validated_data['username'],
                                    jamb=self.validated_data['jamb'],
                                    post_utme=self.validated_data['post_utme'],
                                    aggregate=self.validated_data['aggregate'])
        aggregate_list
        return 

    class Meta:
        model = aggregateList
        fields = '__all__'
