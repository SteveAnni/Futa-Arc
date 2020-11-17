from django.shortcuts import render
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate


from .serializers import createUserSerializer
from rest_framework import serializers, generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.authtoken.models import Token

# Create your views here.
@api_view(['GET'])
def current_user(request):
    """
    get current user instance so as to access it\'s info at the front-end 
    """
    user = request.user
    if user.username == "":
        return Response({
            'user': 'Could not get User instance with the provided credential'
        }, status=status.HTTP_401_UNAUTHORIZED)

    return Response({
        'user': {
            'username': user.username,
            'email': user.email
        }
    }, status=status.HTTP_200_OK)

@api_view(['POST'])
def register_or_login(request):
    credentials = request.data or request.query_params
    # go on to register the user
    serializer = createUserSerializer(data=credentials)
    if serializer.is_valid():
        serializer.save()

        # get the validated username and password to authenticate user immediatly
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']

        # create it credetials matches any
        user = authenticate(username=username,
                            password=password)
            
        # create and assign token to the registered user
        create_token = Token.objects.create(user=user)
        key = create_token.key

        # return a response
        return Response({
            'token': key
        }, status.HTTP_200_OK)

    else:
        response_status = {
            'status': 'Bad Request',
            'status code': int(status.HTTP_400_BAD_REQUEST)
        }
        serializer_errors = serializer.errors

        response_status.update(serializer_errors)
        # raise validations error
        raise serializers.ValidationError(
            response_status
        )
    
        
        
