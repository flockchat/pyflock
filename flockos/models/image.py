# coding: utf-8



from pprint import pformat
from ..utils import to_dict


class Image(object):
    def __init__(self, src=None, width=None, height=None):

        self._src = src
        self._width = width
        self._height = height


    @property
    def src(self):
        return self._src

    @src.setter
    def src(self, src):
        if src is None:
            raise ValueError("Invalid value for `src`, must not be `None`")

        self._src = src

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):

        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):

        self._height = height

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
