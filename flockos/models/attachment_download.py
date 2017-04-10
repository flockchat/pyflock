# coding: utf-8



from pprint import pformat
from ..utils import to_dict


class AttachmentDownload(object):
    def __init__(self, src=None, mime=None, filename=None, size=None):

        self._src = src
        self._mime = mime
        self._filename = filename
        self._size = size


    @property
    def src(self):
        return self._src

    @src.setter
    def src(self, src):
        if src is None:
            raise ValueError("Invalid value for `src`, must not be `None`")

        self._src = src

    @property
    def mime(self):
        return self._mime

    @mime.setter
    def mime(self, mime):

        self._mime = mime

    @property
    def filename(self):
        return self._filename

    @filename.setter
    def filename(self, filename):

        self._filename = filename

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):

        self._size = size

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
