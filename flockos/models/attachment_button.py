# coding: utf-8



from pprint import pformat
from ..utils import to_dict


class AttachmentButton(object):
    def __init__(self, name=None, icon=None, action=None, id=None):

        self._name = name
        self._icon = icon
        self._action = action
        self._id = id


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):

        self._name = name

    @property
    def icon(self):
        return self._icon

    @icon.setter
    def icon(self, icon):

        self._icon = icon

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, action):

        self._action = action

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):

        self._id = id

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
