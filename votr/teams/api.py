from django.http import HttpResponse
from rest_framework import renderers
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import detail_route, list_route

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

    @list_route(methods=['patch'])
    def deactivate_team(self, request):
        success = team_store.deactivate_team(**request.data)
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

    @list_route(methods=['patch'])
    def deactivate_member(self, request):
        success = team_store.deactivate_member(**request.data)
        if success:
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=400)