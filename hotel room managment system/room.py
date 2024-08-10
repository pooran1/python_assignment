from datetime import date

class Room:
    def __init__(self, name, num_of_beds, fare_per_day):
        self.name = name
        self.num_of_beds = num_of_beds
        self.fare_per_day = fare_per_day
        self.bookings = []

    def book_room(self, booking):
        self.bookings.append(booking)

    def is_occupied(self, day):
        for booking in self.bookings:
            if booking.start_date <= day <= booking.end_date:
                return True
        return False

    def is_available(self, date):
        return not self.is_occupied(date)

    def __repr__(self):
        return f"Room(name={self.name}, num_of_beds={self.num_of_beds}, fare_per_day={self.fare_per_day})"
