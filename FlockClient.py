import requests

class FlockClient(object):
    api_url = "https://api.flock-staging.co/v1/"
    token = None
    app_id = None

    def __init__(self, token, app_id):
        if token is None:
            raise ValueError("token is required")
        if app_id is None:
            raise ValueError("app_id is required")
        self.token = token
        self.app_id = app_id

    def send_chat(self, message):
        data = message._get_dict()
        r = self._post_request(data, "chat.sendMessage")
        return r.text

#----------------------------Internal functions---------------------------------
    def _post_request(self, data, endpoint):
        data['token'] = self.token
        data['appid'] = self.app_id
        r = requests.post(self._get_url(endpoint), params=data)
        return r

    def _get_url(self, endpoint):
        return self.api_url + endpoint

    #----------------------------Standard functions-----------------------------------
    def __repr__(self):
        return str(self)

    def __str__(self):
        return "FlockClient[token=%s, app_id=%s]" % (self.token, self.app_id)

