from django.shortcuts import render
from .models import aggregateList
from .serializers import aggregateListSerializer

from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

# Create your views here.
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def aggregate_list(request):
    data = request.data or request.query_params
    data_copy = data.copy()
    data_copy['username'] = request.user
    data_copy['course'] = request.user.profile.course

    serializer = aggregateListSerializer(data=data_copy)

    if serializer.is_valid():
        serializer.save()

        return Response({
            'queryset': serializer.data
        }, status=status.HTTP_200_OK)
    else:
        return Response({
            'queryset': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_aggregate_list(request):
    queryset = aggregateList.objects.all()
    serializer = aggregateListSerializer(queryset, many=True)

    data = serializer.data
    # data['course'] = 
    return Response({
        'queryset': data
    }, status=status.HTTP_200_OK)
