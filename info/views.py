from django.shortcuts import render
from .models import infoModel
from .serializers import infoSerializer

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from django.urls import path


# Create your views here.
@api_view(['GET'])
def infomation(request):
    
    query = request.data or request.query_params
    try:
        queryset = infoModel.objects.all()[:int(query['q'])]
    except Exception as e:
        queryset = infoModel.objects.all()[:5]

    serializer = infoSerializer(queryset, many=True)
    return Response({
        'queryset': serializer.data
    }, status=status.HTTP_200_OK)

