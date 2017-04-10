# coding: utf-8



from __future__ import absolute_import

import os
import sys
import unittest

import flockos
from flockos.rest import ApiException
from flockos.models.html_view import HtmlView


class TestHtmlView(unittest.TestCase):
    """ HtmlView unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testHtmlView(self):
        """
        Test HtmlView
        """
        model = flockos.models.html_view.HtmlView()


if __name__ == '__main__':
    unittest.main()
