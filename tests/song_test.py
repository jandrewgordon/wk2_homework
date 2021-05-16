import unittest
from src.song import *

class TestSong(unittest.TestCase):
    
    def test_can_create_songs(self):
        self.assertEqual("Toxic", Song("Toxic").title)    