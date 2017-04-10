# coding: utf-8



from pprint import pformat
from ..utils import to_dict


class Message(object):
    def __init__(self, _from=None, to=None, id=None, uid=None, timestamp=None, text=None, flockml=None, notification=None, app_id=None, mentions=None, attachments=None, send_as=None):

        self.__from = _from
        self._to = to
        self._id = id
        self._uid = uid
        self._timestamp = timestamp
        self._text = text
        self._flockml = flockml
        self._notification = notification
        self._app_id = app_id
        self._mentions = mentions
        self._attachments = attachments
        self._send_as = send_as


    @property
    def _from(self):
        return self.__from

    @_from.setter
    def _from(self, _from):
        if _from is None:
            raise ValueError("Invalid value for `_from`, must not be `None`")

        self.__from = _from

    @property
    def to(self):
        return self._to

    @to.setter
    def to(self, to):
        if to is None:
            raise ValueError("Invalid value for `to`, must not be `None`")

        self._to = to

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):

        self._id = id

    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, uid):
        if uid is None:
            raise ValueError("Invalid value for `uid`, must not be `None`")

        self._uid = uid

    @property
    def timestamp(self):
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        if timestamp is None:
            raise ValueError("Invalid value for `timestamp`, must not be `None`")

        self._timestamp = timestamp

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        if text is None:
            raise ValueError("Invalid value for `text`, must not be `None`")

        self._text = text

    @property
    def flockml(self):
        return self._flockml

    @flockml.setter
    def flockml(self, flockml):

        self._flockml = flockml

    @property
    def notification(self):
        return self._notification

    @notification.setter
    def notification(self, notification):

        self._notification = notification

    @property
    def app_id(self):
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):

        self._app_id = app_id

    @property
    def mentions(self):
        return self._mentions

    @mentions.setter
    def mentions(self, mentions):

        self._mentions = mentions

    @property
    def attachments(self):
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):

        self._attachments = attachments

    @property
    def send_as(self):
        return self._send_as

    @send_as.setter
    def send_as(self, send_as):

        self._send_as = send_as

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        return to_dict(self.__dict__)

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
