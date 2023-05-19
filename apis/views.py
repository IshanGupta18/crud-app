from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Box
from .serializers import BoxSerializer
from rest_framework import filters
from .serializers import BoxListSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated, IsAdminUser])
def add_box(request):
    serializer = BoxSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(created_by=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated, IsAdminUser])
def update_box(request, box_id):
    try:
        box = Box.objects.get(pk=box_id)
    except Box.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = BoxSerializer(box, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_boxes(request):
    queryset = Box.objects.all()
    serializer = BoxListSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAdminUser])
def list_my_boxes(request):
    queryset = Box.objects.filter(created_by=request.user)
    serializer = BoxListSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_box(request, box_id):
    try:
        box = Box.objects.get(pk=box_id)
    except Box.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.user != box.created_by:
        return Response(status=status.HTTP_403_FORBIDDEN)

    box.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
from django.shortcuts import render

# Create your views here.
