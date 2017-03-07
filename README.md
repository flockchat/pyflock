# flockos
Integrate your apps with flock using this API

- API version: 0.0.4
- Package version: 1.0.0

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com//.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com//.git`)

Then import the package:
```python
import flockos 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import flockos
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import flockos
from flockos.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = flockos.Chat()
token = 'token_example' # str | 
chat = 'chat_example' # str | 
uids = ['uids_example'] # list[str] | 

try:
    api_response = api_instance.fetch_messages(token, chat, uids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Chat->fetch_messages: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.flock-staging.co/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*Chat* | [**fetch_messages**](docs/Chat.md#fetch_messages) | **POST** /chat.fetchMessages | 
*Chat* | [**send_message**](docs/Chat.md#send_message) | **POST** /chat.sendMessage | 
*Groups* | [**get_info**](docs/Groups.md#get_info) | **POST** /groups.getInfo | 
*Groups* | [**get_members**](docs/Groups.md#get_members) | **POST** /groups.getMembers | 
*Groups* | [**list**](docs/Groups.md#list) | **POST** /groups.list | 
*Roster* | [**list_contacts**](docs/Roster.md#list_contacts) | **POST** /roster.listContacts | 
*Users* | [**get_info**](docs/Users.md#get_info) | **POST** /users.getInfo | 
*Users* | [**get_public_profile**](docs/Users.md#get_public_profile) | **POST** /users.getPublicProfile | 


## Documentation For Models

 - [ActionConfig](docs/ActionConfig.md)
 - [Attachment](docs/Attachment.md)
 - [AttachmentButton](docs/AttachmentButton.md)
 - [AttachmentDownload](docs/AttachmentDownload.md)
 - [Error](docs/Error.md)
 - [Group](docs/Group.md)
 - [HtmlView](docs/HtmlView.md)
 - [Image](docs/Image.md)
 - [ImageView](docs/ImageView.md)
 - [Message](docs/Message.md)
 - [PublicProfile](docs/PublicProfile.md)
 - [SendAs](docs/SendAs.md)
 - [UidResponse](docs/UidResponse.md)
 - [User](docs/User.md)
 - [Views](docs/Views.md)
 - [WidgetView](docs/WidgetView.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author



