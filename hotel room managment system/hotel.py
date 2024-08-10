class Hotel:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def total_rooms(self):
        return len(self.rooms)

    def rooms_occupied_today(self, today):
        return sum(1 for room in self.rooms if room.is_occupied(today))

    def rooms_available_today(self, today):
        return self.total_rooms() - self.rooms_occupied_today(today)

    def is_room_available(self, room, date):
        return room.is_available(date)

    def __repr__(self):
        return f"Hotel(name={self.name}, address={self.address}, total_rooms={self.total_rooms()})"
