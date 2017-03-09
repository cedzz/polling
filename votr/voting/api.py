from rest_framework import renderers
from rest_framework import viewsets
import django_filters.rest_framework

from voting.filter import BoothFilter, VotingFilter
from voting.models import Booth, Votes
from voting.serializers import BoothSerializer, VotingSerializer


class BoothViewSet(viewsets.ModelViewSet):

    serializer_class = BoothSerializer
    queryset = Booth.objects.all()
    pagination_class = None
    renderer_classes = (renderers.JSONRenderer, )
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_class = BoothFilter


class VotingViewSet(viewsets.ModelViewSet):

    serializer_class = VotingSerializer
    queryset = Votes.objects.all()
    pagination_class = None
    renderer_classes = (renderers.JSONRenderer, )
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_class = VotingFilter