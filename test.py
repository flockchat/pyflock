from FlockClient import FlockClient
from Message import Message

bala_guid = 'u:7v3ni473vei3nnbi'
deepa_guid = 'u:5qqt9oyaotyrroa5'

f = FlockClient(token='d4c44699-a1ee-457f-bb31-e444656051b2', app_id='987b522b-c1b8-41a4-9d22-5f981c464fef')
m = Message(to_guid=deepa_guid,text="Hello")
print(f, m)
res = f.send_chat(m)
print(res)
