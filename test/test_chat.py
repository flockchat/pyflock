# coding: utf-8



from __future__ import absolute_import

import os
import sys
import unittest

import flockos
from flockos.rest import ApiException
from flockos.apis.chat import Chat


class TestChat(unittest.TestCase):
    """ Chat unit test stubs """

    def setUp(self):
        self.api = flockos.apis.chat.Chat()

    def tearDown(self):
        pass

    def test_send_message(self):
        """
        Test case for send_message

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
