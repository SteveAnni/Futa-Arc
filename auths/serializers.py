from django.contrib.auth.models import User
from rest_framework import serializers, generics

from .models import Profile
class createUserSerializer(serializers.ModelSerializer):
    course = serializers.CharField()
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)


    def validate(self, attrs):
        
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({
                'password': 'Password does not match'
            })
        
        return super().validate(attrs)

    def save(self):
        user = User.objects.create_user(
            username=self.validated_data['username']
            # password=check if they match before seting the password
        )
        user.set_password(self.validated_data['password'])

        profile = Profile.objects.create(
            username=user,
            course=self.validated_data['course'],
        )
        user.save()
        profile.save()

        return user
    class Meta:
        model = User
        fields = '__all__'
