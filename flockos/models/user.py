# coding: utf-8



from pprint import pformat
from ..utils import to_dict


class User(object):
    def __init__(self, id=None, team_id=None, email=None, first_name=None, last_name=None, role=None, timezone=None, profile_image=None):

        self._id = id
        self._team_id = team_id
        self._email = email
        self._first_name = first_name
        self._last_name = last_name
        self._role = role
        self._timezone = timezone
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
    def team_id(self):
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        if team_id is None:
            raise ValueError("Invalid value for `team_id`, must not be `None`")

        self._team_id = team_id

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")

        self._email = email

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
    def role(self):
        return self._role

    @role.setter
    def role(self, role):
        if role is None:
            raise ValueError("Invalid value for `role`, must not be `None`")

        self._role = role

    @property
    def timezone(self):
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        if timezone is None:
            raise ValueError("Invalid value for `timezone`, must not be `None`")

        self._timezone = timezone

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
