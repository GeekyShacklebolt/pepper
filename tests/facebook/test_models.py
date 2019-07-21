# Third party imports
from django.test import TestCase
from tests import factories as f


class TestFacebookPageModel(TestCase):

    def setUp(self):
        self.user = f.create_user(username='test_user', email='test@example.com', password='safestpassword')

    def test_create_facebook_page(self):
        page = {
            "owner": self.user,
            "page_name": "test_page",
            "page_id": "123456789012345",
            "access_token": "alkKJLslfiskIEHikfOOfiffskjosflsjSSFdfsfjsbaeqoialiwqefq"
        }
        page = f.create_facebook_page(**page)
        assert page.id
        assert page.owner.username == 'test_user'
        assert page.page_name == "test_page"
        assert page.page_id == "123456789012345"
        assert page.access_token == "alkKJLslfiskIEHikfOOfiffskjosflsjSSFdfsfjsbaeqoialiwqefq"
        assert str(page) == str(page.page_name)


class TestMessengerLabelModel(TestCase):

    def setUp(self):
        self.user = f.create_user(username='test_user', email='test@example.com', password='safestpassword')
        self.page = f.create_facebook_page(owner=self.user, page_name='test_page')
    def test_create_messenger_label(self):
        label = {
            "owner": self.user,
            "page": self.page,
            "label_name": "test_label"
        }
        label = f.create_messenger_label(**label)
        assert label.id
        assert label.owner == self.user
        assert label.owner.username == "test_user"
        assert label.page == self.page
        assert label.page.page_name == "test_page"
        assert label.label_name == "test_label"
        assert str(label) == str(label.label_name)


class TestPSIDListModel(TestCase):

    def setUp(self):
        self.user = f.create_user(username='test_user', email='test@example.com', password='safestpassword')
        self.page = f.create_facebook_page(owner=self.user, page_name='test_page')
        self.label = f.create_messenger_label(owner=self.user, page=self.page, label_name='test_label')

    def test_create_psid_list(self):
        psid = {
            "page": self.page,
            "label": self.label,
            "psid_list": "12342342342422, 2897839920287684, 928374928374234, 2724188550943785"
        }
        psid = f.create_psid_list(**psid)
        assert psid.id
        assert psid.page == self.page
        assert psid.page.page_name == "test_page"
        assert psid.label == self.label
        assert psid.label.label_name == "test_label"
        assert psid.psid_list == "12342342342422, 2897839920287684, 928374928374234, 2724188550943785"
