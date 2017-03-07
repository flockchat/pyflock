# coding: utf-8



from __future__ import absolute_import

import os
import sys
import unittest

import flockos
from flockos.rest import ApiException
from flockos.models.attachment_download import AttachmentDownload


class TestAttachmentDownload(unittest.TestCase):
    """ AttachmentDownload unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAttachmentDownload(self):
        """
        Test AttachmentDownload
        """
        model = flockos.models.attachment_download.AttachmentDownload()


if __name__ == '__main__':
    unittest.main()
