# Third party imports
from rest_framework.routers import DefaultRouter

# Pepper imports
from pepper.facebook.api import PSIDListViewSet, FacebookPageViewSet, MessengerLabelViewSet

default_router = DefaultRouter(trailing_slash=False)

# Register all the django rest framework viewsets below.
default_router.register('psid', PSIDListViewSet, basename='PSIDListViewSet')
default_router.register('page', FacebookPageViewSet, basename='FacebookPageViewSet')
default_router.register('label', MessengerLabelViewSet, basename='MessengerLabelViewSet')

urlpatterns = default_router.urls
