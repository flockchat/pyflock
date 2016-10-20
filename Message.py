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

    def _get_dict(self):
        data = dict()
        for k, v in self.__dict__.iteritems():
            if v is not None:
                nv = v
                if isinstance(v, Payload):
                    nv = json.dumps(nv._get_dict())
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
