class Room:

    def __init__(self, number, spaces, room_fee):
        self.number = number
        self.spaces = spaces
        self.guests = []
        self.playlist = []
        self.room_fee = room_fee
        self.tab = 0

    def check_in_guest(self, guest):
        if self.spaces >= 1 and guest.wallet >= self.room_fee:
            self.guests.append(guest)
            guest.wallet -= self.room_fee
            self.tab += self.room_fee
            for song in self.playlist:
                if song.title == guest.song:
                    return "Wooh!"
        elif self.spaces == 0:
            print("Not enough spaces")
        elif guest.wallet < self.room_fee:
            print("Not enough money")

    def check_out_guest(self, guest):
        self.guests.remove(guest)

    def add_song_to_playlist(self, song):
        self.playlist.append(song)
    
    def sell_drink(self, guest, drink):
        if guest.wallet >= drink.price:
            self.tab += drink.price
            guest.wallet -= drink.price
