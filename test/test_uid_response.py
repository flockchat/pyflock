# coding: utf-8



from __future__ import absolute_import

import os
import sys
import unittest

import flockos
from flockos.rest import ApiException
from flockos.models.uid_response import UidResponse


class TestUidResponse(unittest.TestCase):
    """ UidResponse unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUidResponse(self):
        """
        Test UidResponse
        """
        model = flockos.models.uid_response.UidResponse()


if __name__ == '__main__':
    unittest.main()
