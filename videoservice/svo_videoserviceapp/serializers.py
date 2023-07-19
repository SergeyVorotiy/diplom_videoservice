from rest_framework import serializers

from .models import VSVideo, VSUser


class VSVideoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VSVideo
        fields = ['name', 'author', 'published_date', 'description', 'likes', 'comments', 'upload']


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VSUser
        fields = ['user', 'black_list', 'ignore_list', 'subscribes']