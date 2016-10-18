import json

class Message(object):
    to_guid = None
    from_guid = None
    text = None
    attachments = None
    send_as = None
    flockml = None
    notification = None
    mentions = None

    def __init__(self, to_guid = None, from_guid = None, text = "", attachments = [], send_as = None, flockml = "", notification = "", mentions = []):
        self.to_guid = to_guid
        self.from_guid = from_guid
        self.text = text
        self.attachments = attachments
        self.send_as = send_as
        self.flockml = flockml
        self.notification = notification
        self.mentions = mentions

    def _get_dict(self):
        data = {}
        if not self.from_guid is None:
            data['from'] = self.from_guid
        data['to'] = self.to_guid
        data['text'] = self.text
        data['attachments'] = json.dumps(self.attachments)
        if not self.send_as is None:
            data['sendAs'] = self.send_as._get_dict
        data['flockml'] = self.flockml
        data['notification'] = self.notification
        data['mentions'] = json.dumps(self.mentions)
        return data

class SendAs(object):
    name = None
    profile_image_url = None

    def __init__(self, name, profile_image_url):
        self.name = name
        self.profile_image = profile_image_url

    def _get_dict(self):
        data = {}
        data['name'] = self.name
        data['profileImage'] = self.profile_image_url
        return data

class Action:
    action_type = None
    url = ""
    desktop_type = ""
    mobile_type = ""
    send_context = None

    def __init__():
        pass

    def add_open_widget(self, url, desktop_type, mobile_type):
        if (url is None) or (desktop_type is None) or (mobile_type is None):
            raise ValueError("url, desktop_type, mobile_type compulsory")
        
        self.action_type = "openWidget"
        self.url = url
        self.desktop_type = desktop_type
        self.mobile_type = mobile_type

    def add_open_browser(self, url, send_context):
        if (url is None) or (send_context is None):
            raise ValueError("url, send_context compulsory")

        self.action_type = "openBrowser"
        self.url = url
        self.send_context = send_context

    def add_dispatch_event(self):
        self.action_type = "sendToAppService"

    def _get_dict(self):
        data = {}
        data['type'] = self.action_type
        if self.url:
            data['url'] = self.url
        if self.desktop_type:
            data['desktopType'] = self.desktop_type
        if self.mobile_type:
            data['mobile_type'] = self.mobile_type
        if self.send_context:
            data['sendContext'] = self.send_context
        return data



