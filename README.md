# pyflock
pyflock is a python client for [FlockOS](https://docs.flock.co/). pyflock currently runs only on Python 2.x

## Install
If you are using virtualenv, use the following command to create the virtualenv:

```
virtualenv venv -p python2
```

Install pyflock using:

```
pip install git+git://github.com/flockchat/pyflock
```

## Usage

### Setup

Import the various classes and methods needed

```python
from pyflock import FlockClient, verify_event_token
from pyflock import Message, SendAs, Attachment, Views, WidgetView, HtmlView, ImageView, Image, Download, Button, OpenWidgetAction, OpenBrowserAction, SendToAppAction
```
Create the flock client (needed for all apis except `verify_event_token`

```python
flock_client = FlockClient(token=bot_token, app_id=app_id) # 

```
`token` can be an user token, For group and user apis, user token is required. For sending messages it can either be an user token or [bot token](https://docs.flock.co/display/flockos/Bots). `to` in message apis can be either [user or group ids](https://docs.flock.co/display/flockos/Identifiers).

### Index

  - [Event Tokens](#verifying-event-index)
  - [Sending Messages](#sending-messages)
  - [Group APIs](#group-apis)
  - [User APIs](#user-apis)

### Verifying event tokens
See [Event Tokens Docs](https://docs.flock.co/display/flockos/Event+Tokens)
```python
event_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBJZCI6Im15LWFwcCIsInVzZXJJZCI6InU6M2QwMDQzMDItYTk3ZC00MDE2LTkxYjQtNmMyMjFiYjQ3ODFkIiwiZXhwIjoyMDAwMDAwMDAwLCJpYXQiOjE0Njk1NDE1NzIsImp0aSI6IjU2OGVhZGY4LTc3ZmMtNDEwOC05MWRhLWQ5NGRhNDZkNzA5YiJ9.-_lhKHsGE_s9a4apLYPgLVWW2UZtD4_-B8yxKtAmmqg'
app_secret = '869eb1d0-419d-4747-98b4-6d81360a6681'
print verify_event_token(event_token = event_token, app_secret = app_secret)
```

### Sending messages

#### Send a simple message
```python
simple_message = Message(to=user_guid,text="Hello, world")
# returns a message id
res = flock_client.send_chat(simple_message)
print(res)
```

#### Send a message using a custom name and profile image
```python
send_as_hal = SendAs(name='HAL-9000', profile_image='https://pbs.twimg.com/profile_images/1788506913/HAL-MC2_400x400.png')
send_as_message = Message(to=user_guid,text="I'm sorry Dave, I'm afraid I can't do that",send_as=send_as_hal)
res = flock_client.send_chat(send_as_message)
print(res)
```

#### Send a widget view
```python
views = Views()
widget = WidgetView(src="http://example.com",height=250)
views.add_widget(widget)

attachment = Attachment(title="Test widget", description="Replace src with your own page", views=views)
# NOTE: attachments is an array of attachment
widget_message = Message(to=user_guid, attachments = [attachment])
res = flock_client.send_chat(widget_message)
print(res)
```

#### Send a HTML view
```python
views = Views()
html = HtmlView(inline="It <b>Works</b>",height=50)
views.add_html(html)

attachment = Attachment(title="Test html", description="Replace inline with your own html", views=views)
# NOTE: attachments is an array of attachment
html_message = Message(to=user_guid, attachments = [attachment])
res = flock_client.send_chat(html_message)
print(res)
```

#### Send a FlockML view
```python
# NOTE: No need for a flockml view object
views = Views()
views.add_flockml("<flockml>FlockML is <b>AWESOME</b></flockml>")

attachment = Attachment(title="Test flockml", description="Replace flockml with your own flockml", views=views)
# NOTE: attachments is an array of attachment
flockml_message = Message(to=user_guid, attachments = [attachment])
res = flock_client.send_chat(flockml_message)
print(res)
```

#### Send a Image view
```python
views = Views()
image = ImageView(original=Image(src="http://library.acropolis.org/wp-content/uploads/2014/11/One_ring.png", width=400, height=400),filename="onering.png")
views.add_image(image)

attachment = Attachment(title="Test image", description="One Ring to rule them all, One Ring to find them, One Ring to bring them all and in the darkness bind them", views=views)
# NOTE: attachments is an array of attachment
image_message = Message(to=user_guid, attachments = [attachment])
res = flock_client.send_chat(image_message)
print(res)
```

#### Send download files
```python
d = Download(src="http://wallpapercave.com/wp/H630T6R.jpg")

views = Views()
views.add_flockml("<flockml>Download the <i>matrix</i></flockml>")

# NOTE: downloads is always a list
attachment = Attachment(title="Test files", downloads=[d], views=views)
files_message = Message(to=user_guid, attachments = [attachment])
res = flock_client.send_chat(files_message)
print(res)
```

#### Button with openwidget, open url & send to app service
```python
b1 = Button(name = "Harry Potter", id="harry", action=OpenWidgetAction(url="https://goo.gl/aygRGf", desktop_type="sidebar"))
b2 = Button(name = "Ron Weasley", id="ron", action=OpenBrowserAction(url="https://goo.gl/gDpMVn", send_context=True))
b3 = Button(name = "Hermione Granger", id="hermione", action=SendToAppAction())
attachment = Attachment(title="Test buttons", buttons=[b1,b2,b3])
button_message = Message(to=user_guid, text="Who is your favourite Harry Potter character?", attachments = [attachment])
res = flock_client.send_chat(button_message)
print(res)
```

#### Now, just for fun, let us change colours
```python
attachment = Attachment(title="Test colour", color="#FF0000", description="It is red!")
color_message = Message(to=user_guid, attachments=[attachment])
res = flock_client.send_chat(color_message)
print(res)
```

### Group APIs

#### Get group info
```python
print flock_client.get_group_info(group_id)
```

#### Get group members
```python
print flock_client.get_group_members(group_id)
```

#### Get groups list of which user is member of 
```python
print flock_client.get_groups()
```

### User APIs

#### Get user info
```python
print flock_client.get_user_info()
```

#### Get all contacts
```python
print flock_client.get_contacts()
```


