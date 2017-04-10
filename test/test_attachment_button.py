# coding: utf-8



from __future__ import absolute_import

import os
import sys
import unittest

import flockos
from flockos.rest import ApiException
from flockos.models.attachment_button import AttachmentButton


class TestAttachmentButton(unittest.TestCase):
    """ AttachmentButton unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAttachmentButton(self):
        """
        Test AttachmentButton
        """
        model = flockos.models.attachment_button.AttachmentButton()


if __name__ == '__main__':
    unittest.main()
