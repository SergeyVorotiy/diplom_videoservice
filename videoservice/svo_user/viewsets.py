from rest_framework import viewsets, permissions

from .models import VideoServiceUser
from .serializers import VSUserPrivateSerializer


class VideoServiceUserViewSet(viewsets.ModelViewSet):
    queryset = VideoServiceUser.objects.all()
    serializer_class = VSUserPrivateSerializer
    permission_classes = permissions.IsAuthenticatedOrReadOnly
