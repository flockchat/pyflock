# coding: utf-8



from pprint import pformat
from ..utils import to_dict


class PublicProfile(object):
    def __init__(self, id=None, first_name=None, last_name=None, profile_image=None):

        self._id = id
        self._first_name = first_name
        self._last_name = last_name
        self._profile_image = profile_image


    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        if first_name is None:
            raise ValueError("Invalid value for `first_name`, must not be `None`")

        self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        if last_name is None:
            raise ValueError("Invalid value for `last_name`, must not be `None`")

        self._last_name = last_name

    @property
    def profile_image(self):
        return self._profile_image

    @profile_image.setter
    def profile_image(self, profile_image):
        if profile_image is None:
            raise ValueError("Invalid value for `profile_image`, must not be `None`")

        self._profile_image = profile_image

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
