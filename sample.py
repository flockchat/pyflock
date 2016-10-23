# DO NOT PANIC

from pyflock import FlockClient, verify_event_token
# You probably want to copy this entire line
from pyflock import Message, SendAs, Attachment, Views, WidgetView, HtmlView, ImageView, Image, Download, Button, OpenWidgetAction, OpenBrowserAction, SendToAppAction

#------ This is pyflock demo. The app id is of a pyflock bot for testing

# The test ids and tokens
bot_token = '3fc42e71-8a5c-4f96-802f-b19566b6af34'
user_guid = 'u:vpvv5pem2mzf25e5'
user2_guid = 'u:5qqt9oyaotyrroa5'
group_guid = 'g:1108515948568984819'
app_id = '6dd7e4b0-3340-4a4f-9243-e47cb8da8ee1'
user_token = bot_token # Store the token against a guid during app install event and retreive it from the user id in event token

#Create a flock client. Needs token and app id for this. You can get the token id and app id when you register. This is for a bot.
flock_client = FlockClient(token=bot_token, app_id=app_id)

res = None

# Send a simple send message
simple_message = Message(to=group_guid,text="Hello, world")
# returns a message id
res = flock_client.send_chat(simple_message)
print(res)

# Send a message using a custom name and profile image
send_as_hal = SendAs(name='HAL-9000', profile_image='https://pbs.twimg.com/profile_images/1788506913/HAL-MC2_400x400.png')
send_as_message = Message(to=group_guid,text="I'm sorry Dave, I'm afraid I can't do that",send_as=send_as_hal)
res = flock_client.send_chat(send_as_message)
print(res)

# Send a widget view
views = Views()
widget = WidgetView(src="http://example.com",height=250)
views.add_widget(widget)

attachment = Attachment(title="Test widget", description="Replace src with your own page", views=views)
# NOTE: attachments is an array of attachment
widget_message = Message(to=group_guid, attachments = [attachment])
res = flock_client.send_chat(widget_message)
print(res)

# Send a HTML view
views = Views()
html = HtmlView(inline="It <b>Works</b>",height=50)
views.add_html(html)

attachment = Attachment(title="Test html", description="Replace inline with your own html", views=views)
# NOTE: attachments is an array of attachment
html_message = Message(to=group_guid, attachments = [attachment])
res = flock_client.send_chat(html_message)
print(res)

# Send a FlockML view
# NOTE: No need for a flockml view object
views = Views()
views.add_flockml("<flockml>FlockML is <b>AWESOME</b></flockml>")

attachment = Attachment(title="Test flockml", description="Replace flockml with your own flockml", views=views)
# NOTE: attachments is an array of attachment
flockml_message = Message(to=group_guid, attachments = [attachment])
res = flock_client.send_chat(flockml_message)
print(res)

# Send a Image view
views = Views()
image = ImageView(original=Image(src="http://library.acropolis.org/wp-content/uploads/2014/11/One_ring.png", width=400, height=400),filename="onering.png")
views.add_image(image)

attachment = Attachment(title="Test image", description="One Ring to rule them all, One Ring to find them, One Ring to bring them all and in the darkness bind them", views=views)
# NOTE: attachments is an array of attachment
image_message = Message(to=group_guid, attachments = [attachment])
res = flock_client.send_chat(image_message)
print(res)

# Send download files
d = Download(src="http://wallpapercave.com/wp/H630T6R.jpg")

views = Views()
views.add_flockml("<flockml>Download the <i>matrix</i></flockml>")

# NOTE: downloads is always a list
attachment = Attachment(title="Test files", downloads=[d], views=views)
files_message = Message(to=group_guid, attachments = [attachment])
res = flock_client.send_chat(files_message)
print(res)

# Button with openwidget, open url & send to app service
b1 = Button(name = "Harry Potter", id="harry", action=OpenWidgetAction(url="https://goo.gl/aygRGf", desktop_type="sidebar"))
b2 = Button(name = "Ron Weasley", id="ron", action=OpenBrowserAction(url="https://goo.gl/gDpMVn", send_context=True))
b3 = Button(name = "Hermione Granger", id="hermione", action=SendToAppAction())
attachment = Attachment(title="Test buttons", buttons=[b1,b2,b3])
button_message = Message(to=group_guid, text="Who is your favourite Harry Potter character?", attachments = [attachment])
res = flock_client.send_chat(button_message)
print(res)

# Now, just for fun, let us change colours
attachment = Attachment(title="Test colour", color="#FF0000", description="It is red!")
color_message = Message(to=group_guid, attachments=[attachment])
res = flock_client.send_chat(color_message)
print(res)

# Get group info
print flock_client.get_group_info(group_guid)

# Get group members
flock_client = FlockClient(token=user_token, app_id=app_id)
print flock_client.get_group_members(group_guid)

# Get groups list of which user is member of 
print flock_client.get_groups()

# Get user info
print flock_client.get_user_info()

# Get all contacts
print flock_client.get_contacts()

# Test JWT token verification
event_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBJZCI6IjFiZjE3ODdkLWEwMzctNDQ1OC04M2E3LTY5ZDY3YjVhMzJkMSIsInVzZXJJZCI6InU6Z3JpMzNwZzNyMXl2aXZqYyIsImV4cCI6MTQ3Nzc3MjE5NywiaWF0IjoxNDc3MTY3Mzk3LCJqdGkiOiJhNTM3MTQ3My0wYTdjLTQxYjctOGYxMS05ZjdmNGY0NDRmMmUifQ.ATZiYS-QAKLagBkWQxRiB9R4MdvWByFTGm6xFfEfIsA'
app_secret = '19177c69-000b-42ed-a2af-1afe1131f769'
print verify_event_token(event_token = event_token, app_secret = app_secret)


