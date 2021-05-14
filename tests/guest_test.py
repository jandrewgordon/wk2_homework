import unittest
from src.guest import *

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guests = [
            {"name": "Andrew"}
        ]

    def test_guest_can_be_added(self):
        self.assertEqual("Andrew", add_guest(self.guests[0]["name"]))
