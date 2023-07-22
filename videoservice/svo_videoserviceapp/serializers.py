from rest_framework import serializers

from .models import VSVideo, VSUser


class VSVideoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VSVideo
        fields = ['name', 'author', 'published_date', 'description', 'likes', 'comments', 'upload']


class AuthorProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VSUser
        fields = ['user', 'black_list', 'ignore_list', 'subscribes']


class AuthorPublicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VSUser
        fields = ['user_username', 'subscribes']
