# Standard imports
import requests

# Pepper imports
import settings


def fetch_label_id(label_name, page):
    """Service to create a messenger label using FB graph API.

    :param label_name: A string containing name of a label to be created.
    :param page: FacebookPage model instance

    :returns: ID of newly created messenger label

    :raises: Abstract exception

    """
    page_access_token = getattr(page, 'access_token')

    url = 'https://graph.facebook.com/v2.11/me/custom_labels?access_token={0}'.format(page_access_token)
    data = {'name': label_name}
    res = requests.post(url=url, data=data)

    if str(res) == '<Response [200]>':
        return res.json()['id']
    else:
        raise Exception("Invalid access token or label name!")


def fetch_users(**validated_data):
    """Service to fetch users' profile using messenger PSID.

    :param validated_data: Serialized data from PSIDListSerializer.

    :returns: Updated validated_data with invalid and valid psid fields.

    """
    url = 'https://graph.facebook.com'
    batch_data = ''
    psid_list = validated_data['psid_list'].split(', ')
    page_access_token = getattr(validated_data['page'], 'access_token')

    for psid in psid_list:
        batch_data = batch_data + '{{"method":"GET", '\
            '"relative_url":"{0}?fields=first_name,last_name&access_token={1}"}},'.format(psid, page_access_token)

    files = {
        'access_token': (None, page_access_token),
        'batch': (None, '[{0}]'.format(batch_data)),
    }

    res = requests.post(url, files=files)

    valid_psid = []
    invalid_psid = []
    for count in range(len(res.json())):
        if res.json()[count]['code'] == 200:
            valid_psid.append(psid_list[count])
        else:
            invalid_psid.append(psid_list[count])
    validated_data['valid_psid'] = ', '.join(valid_psid)
    validated_data['invalid_psid'] = ', '.join(invalid_psid)

    return validated_data


def associate_label(**validated_data):
    """Service to associate messenger labels to users.

    :param validated_data: Serialized data from PSIDListSerializer.

    :returns: Updated validated_data with label_associated_to field.

    """
    url = 'https://graph.facebook.com'
    batch_data = ''
    valid_psid_list = validated_data['valid_psid'].split(', ')
    page_access_token = getattr(validated_data['page'], 'access_token')
    label_id = getattr(validated_data['label'], 'label_id')

    for psid in valid_psid_list:
        batch_data = batch_data + '{{"method":"POST", "relative_url":' \
            '"v3.3/{0}/label?access_token={1}", "body":"user={2}"}},'.format(label_id, page_access_token, psid)

    files = {
        'access_token': (None, page_access_token),
        'batch': (None, '[{0}]'.format(batch_data)),
    }

    res = requests.post(url, files=files)

    associated_psid = []
    for count in range(len(res.json())):
        if res.json()[count]['code'] == 200:
            associated_psid.append(valid_psid_list[count])

    if associated_psid != []:
        validated_data['label_associated_to'] = ', '.join(associated_psid)

    return validated_data


def check_batch_limit(psid_list):
    """Service to check if the batch request is within limit.

    :param psid_list: List of all the given PSIDs.

    """
    psid_count = len(psid_list.split(', '))
    psid_limit = settings.common.FB_BATCH_REQUEST['limit']
    if psid_count > int(psid_limit):
        raise Exception(
            "Facebook batch request limit exceeded. Allowed {0}, received {1}".format(psid_limit, psid_count)
        )
