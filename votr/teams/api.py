from django.http import HttpResponse
from rest_framework import renderers
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response

from teams.filter import TeamFilter, MemberFilter
from teams.models import Teams, Members
from teams.serializers import TeamSerializer, MemberSerializer
from teams.utils import TeamStore

team_store = TeamStore()

class TeamsViewSet(viewsets.ModelViewSet):

    serializer_class = TeamSerializer
    queryset = Teams.objects.all()
    pagination_class = None
    renderer_classes = (renderers.TemplateHTMLRenderer, )
    filter_backends = (DjangoFilterBackend,)
    filter_class = TeamFilter

    @list_route(methods=['patch'])
    def deactivate_team(self, request):
        success = team_store.deactivate_team(**request.data)
        if success:
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=400)

    def list(self, request, *args, **kwargs):
        response = super(TeamsViewSet, self).list(request, *args, **kwargs)
        return Response({"data": response.data}, template_name='team/teams.html')

    def retrieve(self, request, *args, **kwargs):
        response = super(TeamsViewSet, self).retrieve(request, *args, **kwargs)
        return Response({"data": response.data}, template_name='team/team.html')


class MemberViewSet(viewsets.ModelViewSet):

    serializer_class = MemberSerializer
    queryset = Members.objects.all()
    pagination_class = None
    renderer_classes = (renderers.TemplateHTMLRenderer, )
    filter_backends = (DjangoFilterBackend,)
    filter_class = MemberFilter

    @list_route(methods=['patch'])
    def deactivate_member(self, request):
        success = team_store.deactivate_member(**request.data)
        if success:
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=400)

    def list(self, request, *args, **kwargs):
        response = super(MemberViewSet, self).list(request, *args, **kwargs)
        return Response({"data": response.data}, template_name='team/members.html')

    def retrieve(self, request, *args, **kwargs):
        response = super(MemberViewSet, self).retrieve(request, *args, **kwargs)
        return Response({"data": response.data}, template_name='team/member.html')