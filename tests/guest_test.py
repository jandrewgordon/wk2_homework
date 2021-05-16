import unittest
from src.guest import *

class TestGuest(unittest.TestCase):

    def test_can_create_guest(self):
        self.assertEqual("Andrew", Guest("Andrew", 10, "Toxic").name)

