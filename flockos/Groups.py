from Payload import Payload, get_args, get_kwargs

class GroupRequest(Payload):
    def __init__(self, group_id):
        super(GroupRequest, self).__init__(**get_args(locals()))

