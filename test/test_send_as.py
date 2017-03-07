# coding: utf-8



from __future__ import absolute_import

import os
import sys
import unittest

import flockos
from flockos.rest import ApiException
from flockos.models.send_as import SendAs


class TestSendAs(unittest.TestCase):
    """ SendAs unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSendAs(self):
        """
        Test SendAs
        """
        model = flockos.models.send_as.SendAs()


if __name__ == '__main__':
    unittest.main()
