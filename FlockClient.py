import requests

class FlockClient(object):
    api_url = "https://api.flock-staging.co/v1/"

    def __init__(self, token, app_id):
        self.token = token
        self.app_id = app_id

    def send_chat(self, message):
        data = message._get_dict()
        print data
        r = self._post_request(data, "chat.sendMessage")
        return r.text

#----------------------------Internal functions---------------------------------
    def _post_request(self, data, endpoint):
        data['token'] = self.token
        data['appid'] = self.app_id
        print data
        r = requests.post(self._get_url(endpoint), params=data)
        return r

    def _get_url(self, endpoint):
        return self.api_url + endpoint

    #----------------------------Standard functions-----------------------------------
    def __repr__(self):
        return str(self)

    def __str__(self):
        return "FlockClient[app_id=%s, token=%s]" % (self.app_id, self.token)

