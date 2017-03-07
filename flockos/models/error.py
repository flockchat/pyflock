# coding: utf-8



from pprint import pformat
from ..utils import to_dict


class Error(object):
    def __init__(self, error=None, description=None, parameter=None, disabled_by=None):

        self._error = error
        self._description = description
        self._parameter = parameter
        self._disabled_by = disabled_by


    @property
    def error(self):
        return self._error

    @error.setter
    def error(self, error):

        self._error = error

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):

        self._description = description

    @property
    def parameter(self):
        return self._parameter

    @parameter.setter
    def parameter(self, parameter):

        self._parameter = parameter

    @property
    def disabled_by(self):
        return self._disabled_by

    @disabled_by.setter
    def disabled_by(self, disabled_by):

        self._disabled_by = disabled_by

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
