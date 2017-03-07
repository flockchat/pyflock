# coding: utf-8



from __future__ import absolute_import

import os
import sys
import unittest

import flockos
from flockos.rest import ApiException
from flockos.models.image import Image


class TestImage(unittest.TestCase):
    """ Image unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testImage(self):
        """
        Test Image
        """
        model = flockos.models.image.Image()


if __name__ == '__main__':
    unittest.main()
