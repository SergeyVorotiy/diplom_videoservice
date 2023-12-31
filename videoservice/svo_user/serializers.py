from rest_framework import serializers

from .models import VideoServiceUser


class VSUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VideoServiceUser
        fields = ['username', 'first_name', 'last_name', 'avatar']
