# Third party imports
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions

# Pepper imports
from pepper.facebook import serializers

# Relative imports
from . import models


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = serializers.UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer


class FacebookPageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows to feed new Facebook Page credentials.
    """
    permission_classes = (permissions.IsAuthenticated,)
    queryset = models.FacebookPage.objects.all()
    serializer_class = serializers.FacebookPageSerializer


class MessengerLabelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows to create a new Messenger Label.
    """
    permission_classes = (permissions.IsAuthenticated,)
    queryset = models.MessengerLabel.objects.all()
    serializer_class = serializers.MessengerLabelSerializer


class PSIDListViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows to fetch messenger users' profile using PSID and
    associate a messenger label to them.
    """
    permission_classes = (permissions.IsAuthenticated,)
    queryset = models.PSIDList.objects.all()
    serializer_class = serializers.PSIDListSerializer
