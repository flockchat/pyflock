# coding: utf-8



from __future__ import absolute_import

import os
import sys
import unittest

import flockos
from flockos.rest import ApiException
from flockos.models.public_profile import PublicProfile


class TestPublicProfile(unittest.TestCase):
    """ PublicProfile unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPublicProfile(self):
        """
        Test PublicProfile
        """
        model = flockos.models.public_profile.PublicProfile()


if __name__ == '__main__':
    unittest.main()
