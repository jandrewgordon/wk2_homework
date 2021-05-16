class Bar:
    def setUp(self, name):
        self.name = name
        self.rooms = []

    def add_room(self,room):
        self.rooms.append(room)