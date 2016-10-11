import requests, json

class FlockClient:
    _user_token = None
    _api_url = "https://api.flock.co/v1/"
    _app_id

    def _init__(self, user_token, app_id):
        if not user_token:
            raise ValueError("user_token is required")
        if not app_id:
            raise ValueError("app_id is required")
        self._user_token = user_token

    def _get_url(self, endpoint):
        return self._api_url + endpoint

    def send_chat(self, message):
        data = self._dict_from_message(message)
        data['token'] = user_token
        r = requests.post(self._get_url("chat.sendMessage"), )
        return r.text

    def _dict_from_message(message):
        data = {}
        data['from'] = message.from_guid
        data['to'] = message.to_guid
        data['text'] = message.text
        data['attachments'] = json.dumps(message.attachments)
        data['sendAs'] = json.dumps(message.send_as)
        data['flockml'] = message.flockml
        data['notification'] = message.notification
        data['mentions'] = json.dumps(message.mentions)

        return data

