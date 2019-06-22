# Third party imports
from rest_framework.routers import DefaultRouter

# Pepper imports
from pepper.facebook.api import PSIDListViewSet, FacebookPageViewSet, MessengerLabelViewSet

default_router = DefaultRouter(trailing_slash=False)

# Register all the django rest framework viewsets below.
default_router.register('psid', PSIDListViewSet, base_name='PSIDListViewSet')
default_router.register('page', FacebookPageViewSet, base_name='FacebookPageViewSet')
default_router.register('label', MessengerLabelViewSet, base_name='MessengerLabelViewSet')

urlpatterns = default_router.urls
