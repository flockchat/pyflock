import requests
import json
from Message import Payload

class FlockClient(object):
    api_url = "https://api.flock-staging.co/v1/"

    def __init__(self, token, app_id):
        self.token = token
        self.app_id = app_id

    def send_chat(self, message):
        data = message._get_repr()
        print data
        r = self._post_request(data, "chat.sendMessage")
        return r.text

#----------------------------Internal functions---------------------------------
    def _post_request(self, data, endpoint):
        data['token'] = self.token
        data['appid'] = self.app_id
        print "data = %s" % data
        data = self._get_jsonized(data)
        r = requests.post(self._get_url(endpoint), params=data)
        return r

    def _get_jsonized(self, data):
        d = dict()
        for k, v in data.iteritems():
            if isinstance(v, Payload) or isinstance(v, list):
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

