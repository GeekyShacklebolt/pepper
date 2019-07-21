from django.test import TestCase
from pepper.facebook.apps import FacebookConfig


class FacebookConfigTest(TestCase):

    def test_facebook_config(self):
        assert FacebookConfig.name is 'facebook'
        assert FacebookConfig.verbose_name is 'facebook'
