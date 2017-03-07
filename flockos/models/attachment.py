# coding: utf-8



from pprint import pformat
from ..utils import to_dict


class Attachment(object):
    def __init__(self, id=None, app_id=None, title=None, description=None, color=None, views=None, url=None, forward=None, downloads=None, buttons=None):

        self._id = id
        self._app_id = app_id
        self._title = title
        self._description = description
        self._color = color
        self._views = views
        self._url = url
        self._forward = forward
        self._downloads = downloads
        self._buttons = buttons


    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):

        self._id = id

    @property
    def app_id(self):
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):

        self._app_id = app_id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):

        self._title = title

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):

        self._description = description

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):

        self._color = color

    @property
    def views(self):
        return self._views

    @views.setter
    def views(self, views):

        self._views = views

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, url):

        self._url = url

    @property
    def forward(self):
        return self._forward

    @forward.setter
    def forward(self, forward):

        self._forward = forward

    @property
    def downloads(self):
        return self._downloads

    @downloads.setter
    def downloads(self, downloads):

        self._downloads = downloads

    @property
    def buttons(self):
        return self._buttons

    @buttons.setter
    def buttons(self, buttons):

        self._buttons = buttons

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
