from FlockClient import FlockClient
from Message import Message, SendAs

#------ This is pyflock demo. The app id is of a pyflock bot for testing
#Create a flock client. Needs token and app id for this. You can get the token id and app id when you register. This is for a bot.
flock_client = FlockClient(token='d4c44699-a1ee-457f-bb31-e444656051b2', app_id='987b522b-c1b8-41a4-9d22-5f981c464fef')

# The test guids
bala_guid = 'u:7v3ni473vei3nnbi'
deepa_guid = 'u:5qqt9oyaotyrroa5'

# Send a simple send message
simple_message = Message(to=bala_guid,text="Hello, world")
# returns a message id
res = flock_client.send_chat(simple_message)
print(res)

# Send a message using a custom name and profile image
send_as_hal = SendAs(name='HAL-9000', profile_image='https://pbs.twimg.com/profile_images/1788506913/HAL-MC2_400x400.png')
send_as_message = Message(to=bala_guid,text="I'm sorry Dave, I'm afraid I can't do that",send_as=send_as_hal)
res = flock_client.send_chat(send_as_message)
print(res)
