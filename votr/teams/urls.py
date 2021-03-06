from django.conf.urls import url, include
from rest_framework import routers
from teams import api

router = routers.DefaultRouter()
router.register(r'members', api.MemberViewSet)
router.register(r'', api.TeamsViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]