class Message(object):
    to_guid = None
    from_guid = None
    text = None
    attachments = None
    send_as = None
    flockml = None
    notification = None
    mentions = None

    def __init__(self, to_guid = None, from_guid = None, text = "", attachments = [], send_as = {}, flockml = "", notification = "", mentions = []):
        self.to_guid = to_guid
        self.from_guid = from_guid
        self.text = text
        self.attachments = attachments
        self.send_as = send_as
        self.flockml = flockml
        self.notification = notification
        self.mentions = mentions

