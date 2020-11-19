from django.contrib.auth.models import User
from rest_framework import serializers, generics

class createUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        if User.objects.filter(username=attrs['username']).exists():
            raise serializers.ValidationError({
                'username': 'Username is already taken'
            })
        elif attrs['password'] != attrs['confirm_password']:
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
        user.save()

        return user
    class Meta:
        model = User
        fields = '__all__'
