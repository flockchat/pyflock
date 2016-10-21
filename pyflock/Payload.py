def to_camel_case(snake_str):
    components = snake_str.split('_')
    return components[0] + "".join(x.title() for x in components[1:])

def get_args(kw):
    return dict((k,v) for k,v in kw.iteritems() if k <> "self")

def get_kwargs(**kwargs):
    return dict((k,v) for k,v in kwargs.iteritems() if k <> "self")

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
                    nv = [i._get_repr() for i in v]

                nk = to_camel_case(k)
                data[nk] = nv

        return data
 
