# coding: utf-8



from pprint import pformat
from ..utils import to_dict


class Views(object):
    def __init__(self, widget=None, html=None, flockml=None, image=None):

        self._widget = widget
        self._html = html
        self._flockml = flockml
        self._image = image


    @property
    def widget(self):
        return self._widget

    @widget.setter
    def widget(self, widget):

        self._widget = widget

    @property
    def html(self):
        return self._html

    @html.setter
    def html(self, html):

        self._html = html

    @property
    def flockml(self):
        return self._flockml

    @flockml.setter
    def flockml(self, flockml):

        self._flockml = flockml

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, image):

        self._image = image

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
