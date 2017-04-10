# coding: utf-8



from __future__ import absolute_import

import os
import sys
import unittest

import flockos
from flockos.rest import ApiException
from flockos.models.message import Message


class TestMessage(unittest.TestCase):
    """ Message unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMessage(self):
        """
        Test Message
        """
        model = flockos.models.message.Message()


if __name__ == '__main__':
    unittest.main()
