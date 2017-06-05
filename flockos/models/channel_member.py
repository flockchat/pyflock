# coding: utf-8



from pprint import pformat
from ..utils import to_dict


class ChannelMember(object):
    def __init__(self, user_id=None, affiliation=None, public_profile=None):

        self._user_id = user_id
        self._affiliation = affiliation
        self._public_profile = public_profile


    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        if user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")

        self._user_id = user_id

    @property
    def affiliation(self):
        return self._affiliation

    @affiliation.setter
    def affiliation(self, affiliation):
        if affiliation is None:
            raise ValueError("Invalid value for `affiliation`, must not be `None`")

        self._affiliation = affiliation

    @property
    def public_profile(self):
        return self._public_profile

    @public_profile.setter
    def public_profile(self, public_profile):

        self._public_profile = public_profile

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
