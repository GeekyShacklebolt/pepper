# Facebook

## Accept Facebook Page

```
POST /api/page
```

**Parameters**

Name               | Data type | Required | Description
-------------------|-----------|----------|---------------------
id                 | integer   | true     | Unique ID for the facebook page
owner              | integer   | true     | Foreign key to User model
page_name          | text      | true     | Name of facebook page
page_id            | text      | true     | Id of facebook page
access_token       | text      | true     | Access token of facebook page

**Request**
```json
{
    "owner": 7,
    "page_name": "MyPage",
    "page_id": "329429292932042",
    "access_token": "alkKJLslfiskIEHikfOOfiffskjosflsjSSFdfsfjsbaeqoialiwqefq"
}
```

**Response**
Status: 201 Created
```json
{
    "owner": 7,
    "page_name": "MyPage",
    "page_id": "329429292932042",
    "access_token": "alkKJLslfiskIEHikfOOfiffskjosflsjSSFdfsfjsbaeqoialiwqefq"
}
```

## Create Messenger Label

```
POST /api/label
```

**Parameters**

Name               | Data type | Required | Description
-------------------|-----------|----------|---------------------
id                 | integer   | true     | Unique ID for messenger label
owner              | integer   | true     | Foreign key to User model
page               | integer   | true     | Foreign key to FacebookPage model
label_name         | text      | true     | Access token of facebook page
label_id           | text      | true     | Id of messenger label

**Request**
```json
{
    "owner": 7,
    "page": 3,
    "label_name": "MyLabel"
}
```

**Response**
Status: 201 Created
```json
{
    "owner": 7,
    "page": 3,
    "label_name": "MyLabel",
    "label_id": "298374928749922"
}
```

## Fetch users and associate label

```
POST /api/psid
```

**Parameters**

Name               | Data type | Required | Description
-------------------|-----------|----------|---------------------
id                 | integer   | true     | Unique ID for PSID list object
page               | integer   | true     | Foreign key to FacebookPage model
label              | integer   | true     | Foreign key to MessengerLabel model
psid_list          | text      | true     | List of PSIDs
valid_psid         | text      | false    | List of valid PSIDs
invalid_psid       | text      | false    | List of invalid PSIDs
label_associated_to| text      | false    | List of valid PSIDs to which messenger label successfully associated

__NOTE__:
- psid_list: List items are to be entered comma separatedly.

**Request**
```json
{
    "page": 7,
    "label": 3,
    "psid_list": "12342342342422, 2897839920287684, 928374928374234, 2724188550943785"
}
```

**Response**
Status: 201 Created
```json
{
    "page": 7,
    "label": 3,
    "invalid_psid": "12342342342422, 928374928374234",
    "label_associated_to": "2897839920287684, 2724188550943785"
}
```
