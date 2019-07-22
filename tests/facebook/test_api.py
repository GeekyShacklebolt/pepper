# Standard imports
import json
from unittest import mock

# Third party imports
import pytest
from tests import factories as f

pytestmark = pytest.mark.django_db


def test_create_facebook_page(client):
    user = f.create_user(username='test_user', email='test@example.com', password='test')
    client.login(user=user)

    url = '/api/page'
    page = {
        "owner": user.id,
        "page_name": "test_page",
        "page_id": "123456789012345",
        "access_token": "alkKJLslfiskIEHikfOOfiffskjosflsjSSFdfsfjsbaeqoialiwqefq"
    }

    response = client.json.post(url, json.dumps(page))
    expected_keys = [
        'owner', 'page_name', 'page_id', 'access_token',
    ]

    assert response.status_code == 201
    assert set(expected_keys).issubset(response.data.keys())
    response_json = response.data

    assert response_json['owner'] == user.id
    assert response_json['page_name'] == page['page_name']
    assert response_json['page_id'] == page['page_id']
    assert response_json['access_token'] == page['access_token']


@mock.patch('pepper.facebook.services.requests.post')
def test_create_messenger_label(mock_requests_post, client):

    # Test successful creation
    fake_facebook_response_object = mock.MagicMock(**{'json.return_value': {'id': '1234567890'}})
    fake_facebook_response_object.__str__.return_value = '<Response [200]>'

    mock_requests_post.return_value = fake_facebook_response_object

    user = f.create_user(username='test_user', email='test@example.com', password='test')
    client.login(user=user)
    page = f.create_facebook_page()

    url = '/api/label'
    label = {
        "owner": user.id,
        "page": page.id,
        "label_name": "test_label"
    }

    response = client.json.post(url, json.dumps(label))
    expected_keys = [
        'owner', 'page', 'label_name', 'label_id'
    ]

    assert response.status_code == 201
    assert set(expected_keys).issubset(response.data.keys())
    mock_requests_post.assert_called_once()
    response_json = response.data

    assert response_json['owner'] == user.id
    assert response_json['page'] == page.id
    assert response_json['label_name'] == label['label_name']
    assert response_json['label_id'] == '1234567890'

    # Test unsuccessful label creation
    fake_facebook_response_object.__str__.return_value = '<Response [400]>'

    with pytest.raises(Exception) as exc:
        client.json.post(url, json.dumps(label))

    assert exc.value.args[0] == 'Invalid access token or label name!'


@mock.patch('pepper.facebook.services.requests.post')
def test_psid_list_processes(mock_requests_post, client):
    fake_facebook_response_object = mock.MagicMock(**{'json.return_value': [{'code': 200}, {'code': 400}]})
    fake_facebook_response_object.__str__.return_value = '<Response [200]>'

    mock_requests_post.return_value = fake_facebook_response_object

    user = f.create_user(username='test_user', email='test@example.com', password='test')
    client.login(user=user)
    page = f.create_facebook_page(owner=user)
    label = f.create_messenger_label(owner=user, page=page)

    psid = {
        "page": page.id,
        "label": label.id,
        "psid_list": "12342342342422, 98765443210987",
    }

    url = '/api/psid'
    response = client.json.post(url, json.dumps(psid))
    expected_keys = [
        'page', 'label', 'label_associated_to', 'invalid_psid',
    ]

    assert response.status_code == 201
    assert set(expected_keys).issubset(response.data.keys())
    response_json = response.data

    assert response_json['page'] == page.id
    assert response_json['label'] == label.id
    assert response_json['label_associated_to'] == "12342342342422"
    assert response_json['invalid_psid'] == "98765443210987"


@mock.patch('pepper.facebook.services.settings.common.FB_BATCH_REQUEST')
def test_exceeding_batch_limit(mock_FB_BATCH_REQUEST, client):
    user = f.create_user(username='test_user', email='test@example.com', password='test')
    client.login(user=user)
    page = f.create_facebook_page(owner=user)
    label = f.create_messenger_label(owner=user, page=page)

    psid = {
        "page": page.id,
        "label": label.id,
        "psid_list": "12342342342422, 98765443210987",
    }

    url = '/api/psid'

    mock_FB_BATCH_REQUEST.__getitem__.return_value = 1
    with pytest.raises(Exception) as exc:
        client.json.post(url, json.dumps(psid))

    assert exc.value.args[0] == "Facebook batch request limit exceeded. Allowed 1, received 2"
