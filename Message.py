class Message:
    to_guid = None
    from_guid = None
    text = None
    attachments = None
    send_as = None
    flockml = None
    notification = None
    mentions = None

    def __init__(self, to_guid = None, from_guid = None, text = "", attachments = [], send_as = None, flockml = "", notification = "", mentions = []):
        if not (to_guid  || from_guid 

