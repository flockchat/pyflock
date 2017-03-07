# coding: utf-8



from __future__ import absolute_import

import os
import sys
import unittest

import flockos
from flockos.rest import ApiException
from flockos.models.widget_view import WidgetView


class TestWidgetView(unittest.TestCase):
    """ WidgetView unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testWidgetView(self):
        """
        Test WidgetView
        """
        model = flockos.models.widget_view.WidgetView()


if __name__ == '__main__':
    unittest.main()
