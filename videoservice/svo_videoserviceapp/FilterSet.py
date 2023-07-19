import django_filters

from .models import VSUser, VSVideo


class VSAuthorFilter(django_filters.FilterSet):
    user = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = VSUser
        fields = ['user_username',]


class VSVideFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = VSVideo
        fields = ['name',]