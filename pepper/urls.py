# Third party imports
from django.conf.urls import url, include
from rest_framework import routers
from django.contrib import admin

# Pepper imports
from pepper.facebook.api import UserViewSet, GroupViewSet

# Relative imports
from . import api_urls

# Default user and group routers
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # Default API, subjected to change in case of custom 'users' app
    url('', include(router.urls)),

    # Admin
    url('admin/', admin.site.urls),

    # Rest API
    url(r'^api/', include(api_urls)),

    url('api-auth/', include('rest_framework.urls', namespace='facebook')),
]
