# coding: utf-8



from __future__ import absolute_import

import os
import sys
import unittest

import flockos
from flockos.rest import ApiException
from flockos.models.user import User


class TestUser(unittest.TestCase):
    """ User unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUser(self):
        """
        Test User
        """
        model = flockos.models.user.User()


if __name__ == '__main__':
    unittest.main()
