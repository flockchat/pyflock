# coding: utf-8



from __future__ import absolute_import

import os
import sys
import unittest

import flockos
from flockos.rest import ApiException
from flockos.apis.users import Users


class TestUsers(unittest.TestCase):
    """ Users unit test stubs """

    def setUp(self):
        self.api = flockos.apis.users.Users()

    def tearDown(self):
        pass

    def test_get_info(self):
        """
        Test case for get_info

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
