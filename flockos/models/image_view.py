# coding: utf-8



from pprint import pformat
from ..utils import to_dict


class ImageView(object):
    def __init__(self, original=None, thumbnail=None, filename=None):

        self._original = original
        self._thumbnail = thumbnail
        self._filename = filename


    @property
    def original(self):
        return self._original

    @original.setter
    def original(self, original):
        if original is None:
            raise ValueError("Invalid value for `original`, must not be `None`")

        self._original = original

    @property
    def thumbnail(self):
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, thumbnail):

        self._thumbnail = thumbnail

    @property
    def filename(self):
        return self._filename

    @filename.setter
    def filename(self, filename):

        self._filename = filename

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
