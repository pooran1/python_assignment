from datetime import date

from hotel import Hotel
from room import Room
from booking import Booking

if __name__ == "__main__":
    # Create hotel
    hotel = Hotel("Ocean View", "123 Beach Ave")

    # Add rooms
    room1 = Room("101", 2, 100)
    room2 = Room("102", 3, 150)
    room3 = Room("103", 1, 80)

    hotel.add_room(room1)
    hotel.add_room(room2)
    hotel.add_room(room3)

    # Create bookings
    booking1 = Booking(room1, "Alice", date(2024, 7, 19), date(2024, 7, 20))
    booking2 = Booking(room2, "Bob", date(2024, 7, 19), date(2024, 7, 21))

    room1.book_room(booking1)
    room2.book_room(booking2)

    # Print hotel info
    print(hotel)

    # Print rooms info
    for room in hotel.rooms:
        print(room)

    # Print stats
    today = date(2024, 7, 19)
    print(f"Total rooms: {hotel.total_rooms()}")
    print(f"Rooms occupied today: {hotel.rooms_occupied_today(today)}")
    print(f"Rooms available today: {hotel.rooms_available_today(today)}")

    # Check room availability on a future date
    future_date = date(2024, 7, 22)
    print(f"Room 101 available on {future_date}: {hotel.is_room_available(room1, future_date)}")
    print(f"Room 102 available on {future_date}: {hotel.is_room_available(room2, future_date)}")
    print(f"Room 103 available on {future_date}: {hotel.is_room_available(room3, future_date)}")
