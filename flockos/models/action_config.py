# coding: utf-8



from pprint import pformat
from ..utils import to_dict


class ActionConfig(object):
    def __init__(self, type=None, url=None, desktop_type=None, mobile_type=None, send_context=None):

        self._type = type
        self._url = url
        self._desktop_type = desktop_type
        self._mobile_type = mobile_type
        self._send_context = send_context


    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, url):

        self._url = url

    @property
    def desktop_type(self):
        return self._desktop_type

    @desktop_type.setter
    def desktop_type(self, desktop_type):

        self._desktop_type = desktop_type

    @property
    def mobile_type(self):
        return self._mobile_type

    @mobile_type.setter
    def mobile_type(self, mobile_type):

        self._mobile_type = mobile_type

    @property
    def send_context(self):
        return self._send_context

    @send_context.setter
    def send_context(self, send_context):

        self._send_context = send_context

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
