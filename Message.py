import json

def to_camel_case(snake_str):
    components = snake_str.split('_')
    return components[0] + "".join(x.title() for x in components[1:])

def get_args(kw):
    return dict((k,v) for k,v in kw.iteritems() if k <> "self")

class Payload(object):
    def __init__(self, **kwargs):
        for kw,arg in kwargs.iteritems():
            setattr(self, kw, arg)

    def _get_repr(self):
        data = dict()
        for k, v in self.__dict__.iteritems():
            if v is not None:
                nv = v
                if isinstance(v, Payload):
                    nv = v._get_repr()
                elif isinstance(v, list):
                    nv = json.dumps([i._get_repr() for i in v])

                nk = to_camel_case(k)
                data[nk] = nv

        return data
    
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

