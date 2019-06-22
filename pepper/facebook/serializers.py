# Third party imports
from django.contrib.auth.models import User, Group
from rest_framework import serializers


# Relative imports
from . import models
from . import services


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class FacebookPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FacebookPage
        fields = ('owner', 'page_name', 'page_id', 'access_token')


class MessengerLabelSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        validated_data['label_id'] = services.fetch_label_id(
            validated_data['label_name'], validated_data['page'],
        )
        return models.MessengerLabel.objects.create(**validated_data)

    class Meta:
        model = models.MessengerLabel
        fields = ('owner', 'page', 'label_name', 'label_id')
        extra_kwargs = {
            'label_id': {'read_only': True},
        }


class PSIDListSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        services.check_batch_limit(validated_data['psid_list'])
        validated_data = services.fetch_users(**validated_data)
        validated_data = services.associate_label(**validated_data)
        return models.PSIDList.objects.create(**validated_data)

    class Meta:
        model = models.PSIDList
        fields = ('page', 'label', 'psid_list', 'invalid_psid', 'label_associated_to')
        extra_kwargs = {
            'psid_list': {'write_only': True},
            'invalid_psid': {'read_only': True},
            'label_associated_to': {'read_only': True},
        }
