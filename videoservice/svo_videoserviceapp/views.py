from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import VSUser, VSComment, VSVideo
from .serializers import VSVideoSerializer, AuthorProfileSerializer


@api_view(['GET'])
def get_public_video_list(request):
    public_video_list = VSVideo.objects.get(is_public=True)
    serializer = VSVideoSerializer(public_video_list, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'PATCH'])
@permission_classes(IsAuthenticated)
def user_profile(request):
    try:
        user = VSUser.objects.get(username=request.user.username)
    except VSUser.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        user = VSUser.objects.get(user=request.user.username)
        serializer = AuthorProfileSerializer(user)

        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PATCH':
        serializer = AuthorProfileSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
