from rest_framework import renderers
from rest_framework import viewsets
import django_filters.rest_framework

from teams.filter import TeamFilter, MemberFilter
from teams.models import Teams
from teams.serializers import TeamSerializer, MemberSerializer


class TeamsViewSet(viewsets.ModelViewSet):

    serializer_class = TeamSerializer
    queryset = Teams.objects.all()
    pagination_class = None
    renderer_classes = (renderers.JSONRenderer, )
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_class = TeamFilter


class MemberViewSet(viewsets.ModelViewSet):

    serializer_class = MemberSerializer
    queryset = Teams.objects.all()
    pagination_class = None
    renderer_classes = (renderers.JSONRenderer, )
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_class = MemberFilter