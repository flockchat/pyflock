import requests
import json
from Message import Payload
from Groups import GroupRequest
import jwt
import urllib
import base64

def _process_token_part(p):
    while len(p) % 4 != 0:
        p += "="
    p = base64.b64encode(base64.urlsafe_b64decode(p))
    return p

def _get_padded_token(token):
    parts = token.split('.')
    processed_parts = [_process_token_part(p) for p in parts]
    return '.'.join(processed_parts)

def verify_event_token(event_token, app_secret):
    processed_token = _get_padded_token(event_token)
    return jwt.decode(processed_token, app_secret, algorithms=['HS256'])

class FlockClient(object):
    api_url = "https://api.flock.co/v1/"

    def __init__(self, token, app_id):
        self.token = token
        self.app_id = app_id

    def send_chat(self, message):
        data = message._get_repr()
        r = self._post_request(data, "chat.sendMessage")
        return json.loads(r.text)
    
    def get_group_info(self, group_id):
        data = GroupRequest(group_id=group_id)._get_repr()
        r = self._post_request(data, "groups.getInfo")
        return json.loads(r.text)

    def get_group_members(self, group_id):
        data = GroupRequest(group_id=group_id)._get_repr()
        r = self._post_request(data, "groups.getMembers")
        return json.loads(r.text)

    def get_groups(self):
        r = self._post_request({}, "groups.list")
        return json.loads(r.text)

    def get_user_info(self):
        r = self._post_request({}, "users.getInfo")
        return json.loads(r.text)

    def get_contacts(self):
        r = self._post_request({}, "roster.listContacts")
        return json.loads(r.text)

#----------------------------Internal functions---------------------------------
    def _post_request(self, data, endpoint):
        data['token'] = self.token
        data['appid'] = self.app_id
        data = self._get_jsonized(data)
        r = requests.post(self._get_url(endpoint), params=data)
        return r

    def _get_jsonized(self, data):
        d = dict()
        for k, v in data.iteritems():
            if isinstance(v, dict) or isinstance(v, list):
                d[k] = json.dumps(v)
            else:
                d[k] = v

        return d

    def _get_url(self, endpoint):
        return self.api_url + endpoint
    #----------------------------Standard functions-----------------------------------
    def __repr__(self):
        return str(self)

    def __str__(self):
        return "FlockClient[app_id=%s, token=%s]" % (self.app_id, self.token)

