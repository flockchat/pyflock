# coding: utf-8



from __future__ import absolute_import

import os
import sys
import unittest

import flockos
from flockos.rest import ApiException
from flockos.models.image_view import ImageView


class TestImageView(unittest.TestCase):
    """ ImageView unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testImageView(self):
        """
        Test ImageView
        """
        model = flockos.models.image_view.ImageView()


if __name__ == '__main__':
    unittest.main()
