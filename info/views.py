from django.shortcuts import render
from .models import infoModel, aggregateList
from .serializers import infoSerializer, aggregateListSerializer

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

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

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def aggregate_list(request):
    data = request.data or request.query_params
    queryset = aggregateList.objects.all()
    serializer = aggregateListSerializer(data=data)

    if serializer.is_valid():
        serializer.save()

        return Response({
            'queryset': serializer.data
        }, status=status.HTTP_200_OK)
    else:
        return Response({
            'queryset': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
