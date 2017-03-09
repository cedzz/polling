from rest_framework import renderers
from rest_framework import viewsets
import django_filters.rest_framework

from sprints.filter import ProjectsFilter, SprintsFilter
from sprints.models import Projects, Sprints
from sprints.serializers import ProjectsSerializer, SprintsSerializer


class ProjectsViewSet(viewsets.ModelViewSet):

    serializer_class = ProjectsSerializer
    queryset = Projects.objects.all()
    pagination_class = None
    renderer_classes = (renderers.JSONRenderer, )
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_class = ProjectsFilter


class SprintsViewSet(viewsets.ModelViewSet):

    serializer_class = SprintsSerializer
    queryset = Sprints.objects.all()
    pagination_class = None
    renderer_classes = (renderers.JSONRenderer, )
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_class = SprintsFilter