from django.http import HttpResponse
from rest_framework import renderers
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import detail_route

from teams.filter import TeamFilter, MemberFilter
from teams.models import Teams, Members
from teams.serializers import TeamSerializer, MemberSerializer
from teams.utils import TeamStore

team_store = TeamStore()

class TeamsViewSet(viewsets.ModelViewSet):

    template_name = 'team.html'
    serializer_class = TeamSerializer
    queryset = Teams.objects.all()
    pagination_class = None
    renderer_classes = (renderers.JSONRenderer, )
    filter_backends = (DjangoFilterBackend,)
    filter_class = TeamFilter

    @detail_route(methods=['post'])
    def deactivate_team(self, request, pk=None):
        success = team_store.deactivate_team(pk=pk)
        if success:
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=400)


class MemberViewSet(viewsets.ModelViewSet):

    template_name = 'member.html'
    serializer_class = MemberSerializer
    queryset = Members.objects.all()
    pagination_class = None
    renderer_classes = (renderers.JSONRenderer, )
    filter_backends = (DjangoFilterBackend,)
    filter_class = MemberFilter

    @detail_route(methods=['post'])
    def deactivate_member(self, request, pk=None):
        success = team_store.deactivate_member(pk=pk)
        if success:
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=400)