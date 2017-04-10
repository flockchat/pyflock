# coding: utf-8



from pprint import pformat
from ..utils import to_dict


class UidResponse(object):
    def __init__(self, uid=None):

        self._uid = uid


    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, uid):

        self._uid = uid

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
