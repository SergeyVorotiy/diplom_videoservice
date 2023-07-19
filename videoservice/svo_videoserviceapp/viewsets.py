from rest_framework import viewsets, permissions

from .models import VSUser, VSVideo
from .serializers import VSVideoSerializer, AuthorSerializer


class VSVideoViewSet(viewsets.ModelViewSet):
    queryset = VSVideo.objects.all().ordered_by('-date_joined')
    serializer_class = VSVideoSerializer
    permission_classes = permissions.IsAuthenticatedOrReadOnly


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = VSUser.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = permissions.IsAuthenticatedOrReadOnly
