# DO NOT PANIC

from FlockClient import FlockClient
# You probably want to copy this entire line
from Message import Message, SendAs, Attachment, Views, WidgetView, HtmlView, ImageView, Image, Download, Button, OpenWidgetAction, OpenBrowserAction, SendToAppAction


#------ This is pyflock demo. The app id is of a pyflock bot for testing
#Create a flock client. Needs token and app id for this. You can get the token id and app id when you register. This is for a bot.
flock_client = FlockClient(token='d4c44699-a1ee-457f-bb31-e444656051b2', app_id='987b522b-c1b8-41a4-9d22-5f981c464fef')

res = None

# The test guids
bala_guid = 'u:7v3ni473vei3nnbi'
deepa_guid = 'u:5qqt9oyaotyrroa5'
group_id = 'g:2213136127433909016'

# Send a simple send message
simple_message = Message(to=bala_guid,text="Hello, world")
# returns a message id
#res = flock_client.send_chat(simple_message)
print(res)

# Send a message using a custom name and profile image
send_as_hal = SendAs(name='HAL-9000', profile_image='https://pbs.twimg.com/profile_images/1788506913/HAL-MC2_400x400.png')
send_as_message = Message(to=bala_guid,text="I'm sorry Dave, I'm afraid I can't do that",send_as=send_as_hal)
#res = flock_client.send_chat(send_as_message)
print(res)

# Send a widget view
views = Views()
widget = WidgetView(src="http://example.com",height=250)
views.add_widget(widget)

attachment = Attachment(title="Test widget", description="Replace src with your own page", views=views)
# NOTE: attachments is an array of attachment
widget_message = Message(to=bala_guid, attachments = [attachment])
#res = flock_client.send_chat(widget_message)
print(res)

# Send a HTML view
views = Views()
html = HtmlView(inline="It <b>Works</b>",height=50)
views.add_html(html)

attachment = Attachment(title="Test html", description="Replace inline with your own html", views=views)
# NOTE: attachments is an array of attachment
html_message = Message(to=bala_guid, attachments = [attachment])
#res = flock_client.send_chat(html_message)
print(res)

# Send a FlockML view
# NOTE: No need for a flockml view object
views = Views()
views.add_flockml("<flockml>FlockML is <b>AWESOME</b></flockml>")

attachment = Attachment(title="Test flockml", description="Replace flockml with your own flockml", views=views)
# NOTE: attachments is an array of attachment
flockml_message = Message(to=bala_guid, attachments = [attachment])
#res = flock_client.send_chat(flockml_message)
print(res)

# Send a Image view
views = Views()
image = ImageView(original=Image(src="http://library.acropolis.org/wp-content/uploads/2014/11/One_ring.png", width=400, height=400),filename="onering.png")
views.add_image(image)

attachment = Attachment(title="Test image", description="One Ring to rule them all, One Ring to find them, One Ring to bring them all and in the darkness bind them", views=views)
# NOTE: attachments is an array of attachment
image_message = Message(to=bala_guid, attachments = [attachment])
#res = flock_client.send_chat(image_message)
print(res)

# Send download files
d = Download(src="http://wallpapercave.com/wp/H630T6R.jpg")

views = Views()
views.add_flockml("<flockml>Download the <i>matrix</i></flockml>")

# NOTE: downloads is always a list
attachment = Attachment(title="Test files", downloads=[d], views=views)
files_message = Message(to=bala_guid, attachments = [attachment])
#res = flock_client.send_chat(files_message)
print(res)

# Button with openwidget, open url & send to app service
b1 = Button(name = "Harry Potter", id="harry", action=OpenWidgetAction(url="https://goo.gl/aygRGf", desktop_type="sidebar"))
b2 = Button(name = "Ron Weasley", id="ron", action=OpenBrowserAction(url="https://goo.gl/gDpMVn", send_context=True))
b3 = Button(name = "Hermione Granger", id="hermione", action=SendToAppAction())
attachment = Attachment(title="Test buttons", buttons=[b1,b2,b3])
button_message = Message(to=bala_guid, text="Who is your favourite Harry Potter character?", attachments = [attachment])
#res = flock_client.send_chat(button_message)
print(res)

# Now, just for fun, let us change colours
attachment = Attachment(title="Test colour", color="#FF0000", description="It is red!")
color_message = Message(to=bala_guid, attachments=[attachment])
#res = flock_client.send_chat(color_message)
print(res)

# Get group info
print flock_client.get_group_info(group_id)
