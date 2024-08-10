class Booking:
    def __init__(self, room, guest_name, start_date, end_date):
        self.room = room
        self.guest_name = guest_name
        self.start_date = start_date
        self.end_date = end_date

    def __repr__(self):
        return f"Booking(guest_name={self.guest_name}, start_date={self.start_date}, end_date={self.end_date})"
