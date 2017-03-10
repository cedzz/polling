from rest_framework import renderers
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from teams.filter import TeamFilter, MemberFilter
from teams.models import Teams, Members
from teams.serializers import TeamSerializer, MemberSerializer


class TeamsViewSet(viewsets.ModelViewSet):

    template_name = 'team.html'
    serializer_class = TeamSerializer
    queryset = Teams.objects.all()
    pagination_class = None
    renderer_classes = (renderers.JSONRenderer, )
    filter_backends = (DjangoFilterBackend,)
    filter_class = TeamFilter


class MemberViewSet(viewsets.ModelViewSet):

    template_name = 'member.html'
    serializer_class = MemberSerializer
    queryset = Members.objects.all()
    pagination_class = None
    renderer_classes = (renderers.JSONRenderer, )
    filter_backends = (DjangoFilterBackend,)
    filter_class = MemberFilter