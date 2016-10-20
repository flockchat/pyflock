import json

class Message(object):
    def __init__(self, to = None, text = "", attachments = [], send_as = None, flockml = None, notification = None, mentions = None):
        self.to = to
        self.text = text
        self.flockml = flockml
        self.notification = notification
        self.mentions = mentions
        self.send_as = send_as
        self.attachments = attachments

    def _get_dict(self):
        data = {}
        data['to'] = self.to
        data['text'] = self.text
        if self.flockml is not None:
            data['flockml'] = self.flockml
        if self.notification is not None:
            data['notification'] = self.notification
        if self.mentions is not None:
            data['mentions'] = json.dumps(self.mentions)
        if self.send_as is not None:
            data['sendAs'] = self.send_as._get_dict
        if self.attachments is not None:
            data['attachments'] = json.dumps(self.attachments)
        return data

class SendAs(object):
    def __init__(self, name, profile_image_url):
        self.name = name
        self.profile_image = profile_image_url

    def _get_dict(self):
        data = {}
        data['name'] = self.name
        data['profileImage'] = self.profile_image_url
        return data

