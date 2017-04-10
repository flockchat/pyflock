# coding: utf-8



from __future__ import absolute_import

import os
import sys
import unittest

import flockos
from flockos.rest import ApiException
from flockos.models.group import Group


class TestGroup(unittest.TestCase):
    """ Group unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGroup(self):
        """
        Test Group
        """
        model = flockos.models.group.Group()


if __name__ == '__main__':
    unittest.main()
