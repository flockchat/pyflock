# coding: utf-8



from __future__ import absolute_import

import os
import sys
import unittest

import flockos
from flockos.rest import ApiException
from flockos.models.action_config import ActionConfig


class TestActionConfig(unittest.TestCase):
    """ ActionConfig unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testActionConfig(self):
        """
        Test ActionConfig
        """
        model = flockos.models.action_config.ActionConfig()


if __name__ == '__main__':
    unittest.main()
