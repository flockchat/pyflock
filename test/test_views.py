# coding: utf-8



from __future__ import absolute_import

import os
import sys
import unittest

import flockos
from flockos.rest import ApiException
from flockos.models.views import Views


class TestViews(unittest.TestCase):
    """ Views unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testViews(self):
        """
        Test Views
        """
        model = flockos.models.views.Views()


if __name__ == '__main__':
    unittest.main()
