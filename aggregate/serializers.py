from rest_framework import serializers
from .models import aggregateList
from django.contrib.auth.models import User



class aggregateListSerializer(serializers.ModelSerializer):
    username = serializers.SlugRelatedField(
        slug_field='username',
        queryset = User.objects.all()
    )

    def save(self):
        if aggregateList.objects.filter(username=self.validated_data['username']).exists():
            updated_aggregate_list = aggregateList.objects.filter(username=self.validated_data['username']).update(
                                                                jamb=self.validated_data['jamb'],
                                                                post_utme=self.validated_data['post_utme'],
                                                                aggregate=self.validated_data['aggregate'])
            return updated_aggregate_list
        else:
            aggregate_list = aggregateList.objects.create(
                username=self.validated_data['username'],
                course=self.validated_data['course'],
                jamb=self.validated_data['jamb'],
                post_utme=self.validated_data['post_utme'],
                aggregate=self.validated_data['aggregate'])
            return aggregate_list

    class Meta:
        model = aggregateList
        fields = '__all__'

class getAggregateSerializer(serializers.ModelSerializer):
    class Meta:
        model = aggregateList
        fields = '__all__'
