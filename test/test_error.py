# coding: utf-8



from __future__ import absolute_import

import os
import sys
import unittest

import flockos
from flockos.rest import ApiException
from flockos.models.error import Error


class TestError(unittest.TestCase):
    """ Error unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testError(self):
        """
        Test Error
        """
        model = flockos.models.error.Error()


if __name__ == '__main__':
    unittest.main()
