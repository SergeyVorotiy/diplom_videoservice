from rest_framework import viewsets, permissions

from .models import VideoServiceUser
from .serializers import VSUserSerializer


class VideoServiceUserViewSet(viewsets.ModelViewSet):
    queryset = VideoServiceUser.objects.all()
    serializer_class = VSUserSerializer
    permission_classes = permissions.IsAuthenticatedOrReadOnly
