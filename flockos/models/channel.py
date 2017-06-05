# coding: utf-8



from pprint import pformat
from ..utils import to_dict


class Channel(object):
    def __init__(self, id=None, name=None, member_count=None, profile_image=None):

        self._id = id
        self._name = name
        self._member_count = member_count
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
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def member_count(self):
        return self._member_count

    @member_count.setter
    def member_count(self, member_count):
        if member_count is None:
            raise ValueError("Invalid value for `member_count`, must not be `None`")

        self._member_count = member_count

    @property
    def profile_image(self):
        return self._profile_image

    @profile_image.setter
    def profile_image(self, profile_image):

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
