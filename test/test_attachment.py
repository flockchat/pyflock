# coding: utf-8



from __future__ import absolute_import

import os
import sys
import unittest

import flockos
from flockos.rest import ApiException
from flockos.models.attachment import Attachment


class TestAttachment(unittest.TestCase):
    """ Attachment unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAttachment(self):
        """
        Test Attachment
        """
        model = flockos.models.attachment.Attachment()


if __name__ == '__main__':
    unittest.main()
