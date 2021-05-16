import unittest
from src.room import *
from src.bar import *
from src.guest import *
from src.song import *
from src.drink import *

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Andrew", 6, "Toxic")
        self.guest2 = Guest("Saad", 4, "Total Eclipse of the Heart")
        self.room = Room(1, 5, 6)
        self.room2 = Room(2, 0, 10)
        self.song = Song("Toxic")
        self.song2 = Song("Total Eclipse of the Heart")
        self.drink = Drink("Beer", 4)
        self.drink2 = Drink("Wine", 6)

    def test_can_create_rooms(self):
        self.assertEqual(1, Room(1, 5, 6).number)    

    def test_guest_checked_in(self):
        self.room.check_in_guest(self.guest)
        self.assertEqual(len(self.room.guests), 1)

    def test_guest_checked_out(self):
        self.room.check_in_guest(self.guest)
        self.room.check_out_guest(self.guest)
        self.assertEqual(len(self.room.guests), 0)

    def test_song_added_to_playlist(self):
        self.room.add_song_to_playlist(self.song)
        self.assertEqual(len(self.room.playlist), 1)

    def test_room_is_full(self):
        self.room2.check_in_guest(self.guest)
        self.assertEqual(len(self.room2.guests), 0)

    def test_guest_doesnt_have_enough_money(self):
        self.room.check_in_guest(self.guest2)
        self.assertEqual(len(self.room.guests), 0)

    def test_guest_woos_at_their_favourite_song(self):
        self.room.add_song_to_playlist(self.song)
        self.assertEqual(self.room.check_in_guest(self.guest), "Wooh!")

    def test_sell_drink(self):
        self.room.sell_drink(self.guest, self.drink)
        self.assertEqual(self.room.tab, 4)

    def test_room_fee_added_to_tab(self):
        self.room.check_in_guest(self.guest)
        self.assertEqual(self.room.tab, 6)

 
    