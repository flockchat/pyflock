# coding: utf-8



from __future__ import absolute_import

import os
import sys
import unittest

import flockos
from flockos.rest import ApiException
from flockos.apis.roster import Roster


class TestRoster(unittest.TestCase):
    """ Roster unit test stubs """

    def setUp(self):
        self.api = flockos.apis.roster.Roster()

    def tearDown(self):
        pass

    def test_list_contacts(self):
        """
        Test case for list_contacts

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
