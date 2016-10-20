import json
from Payload import Payload, get_args, get_kwargs

   
class Message(Payload):
    def __init__(self, to = None, text = "", attachments = None, send_as = None, flockml = None, notification = None, mentions = None):
        super(Message, self).__init__(**get_args(locals()))

class SendAs(Payload):
    def __init__(self, name, profile_image):
        super(SendAs, self).__init__(**get_args(locals()))

class Attachment(Payload):
    def __init__(self, id = None, title = None, description = None, color = None, views = None, url = None, forward = None, downloads = None, buttons = None):
        super(Attachment, self).__init__(**get_args(locals()))

class Views(Payload):
    def __init__(self):
        super(Views, self).__init__()

    def add_widget(self, w):
        self.widget = w

    def add_html(self, h):
        self.html = h

    def add_flockml(self, f):
        self.flockml = f

    def add_image(self, i):
        self.image = i

    def add_downloads(self, d):
        self.downloads = d

class View(Payload):
    def __init__(self, **kwargs):
        super(View, self).__init__(**kwargs)

class WidgetView(View):
    def __init__(self, src, height, width = None):
        super(WidgetView, self).__init__(**get_args(locals()))

class HtmlView(View):
    def __init__(self, inline, height, width = None):
        super(HtmlView, self).__init__(**get_args(locals()))

class Image(Payload):
    def __init__(self, src, height = None, width = None):
        super(Image, self).__init__(**get_args(locals()))

class ImageView(View):
    def __init__(self, original, thumbnail = None, filename = None):
        super(ImageView, self).__init__(**get_args(locals()))

class Download(Payload):
    def __init__(self, src, mime = None, filename = None, size = None):
        super(Download, self).__init__(**get_args(locals()))

class Button(Payload):
    def __init__(self, name, action, icon = None, id = None):
        super(Button, self).__init__(**get_args(locals()))

class ButtonAction(Payload):
    def __init__(self, type, **kwargs):
        super(ButtonAction, self).__init__(**get_kwargs(type=type, **kwargs))

class OpenWidgetAction(ButtonAction):
    def __init__(self, url, desktop_type, mobile_type = "modal"):
        super(OpenWidgetAction, self).__init__(type="openWidget", **get_args(locals()))

class OpenBrowserAction(ButtonAction):
    def __init__(self, url, send_context = None):
        super(OpenBrowserAction, self).__init__(type="openBrowser", **get_args(locals()))

class SendToAppAction(ButtonAction):
    def __init__(self):
        super(SendToAppAction, self).__init__(type="sendToAppService", **get_args(locals()))

