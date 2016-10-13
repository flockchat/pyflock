import requests, json

class FlockClient(object):
    _api_url = "https://api.flock-staging.co/v1/"
    _token = None
    _app_id = None

    def __init__(self, token, app_id):
        if token is None:
            raise ValueError("token is required")
        if app_id is None:
            raise ValueError("app_id is required")
        self._token = token
        self._app_id = app_id

    def send_chat(self, message):
        data = self._dict_from_message(message)
        r = self._post_request(data, "chat.sendMessage")
        return r.text

#----------------------------Internal functions---------------------------------
    def _post_request(self, data, endpoint):
        data['token'] = self._token
        data['appid'] = self._app_id
        r = requests.post(self._get_url(endpoint), params=data)
        print r
        return r

    def _get_url(self, endpoint):
        return self._api_url + endpoint

    def _dict_from_message(self, message):
        data = {}
        if not message.from_guid is None:
            data['from'] = message.from_guid
        data['to'] = message.to_guid
        data['text'] = message.text
        data['attachments'] = json.dumps(message.attachments)
        if not message.send_as is None:
            data['sendAs'] = json.dumps(message.send_as)
        data['flockml'] = message.flockml
        data['notification'] = message.notification
        data['mentions'] = json.dumps(message.mentions)

        return data

#----------------------------Standard functions-----------------------------------
    def __repr__(self):
        return str(self)

    def __str__(self):
        return "FlockClient[token=%s, app_id=%s" % (self._token, self._app_id)

