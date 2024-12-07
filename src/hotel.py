from room import Room
from guest import Guest
from reservation import Reservation

class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = []
        self.reservations = []

    def add_room(self, room):
        self.rooms.append(room)

    def add_guest(self, guest):
        self.guests.append(guest)

    def make_reservation(self, reservation):
        if reservation.room.status == "Available":
            reservation.room.status = "Occupied"
            self.reservations.append(reservation)
            print(f"Reservation {reservation.reservation_id} created successfully!")
        else:
            print(f"Room {reservation.room.room_id} is not available!")

    def cancel_reservation(self, reservation_id):
        for reservation in self.reservations:
            if reservation.reservation_id == reservation_id:
                reservation.status = "Cancelled"
                reservation.room.status = "Available"
                print(f"Reservation {reservation_id} has been cancelled.")
                return
        print(f"Reservation {reservation_id} not found.")

    def list_rooms(self):
        for room in self.rooms:
            print(room)

    def list_guests(self):
        for guest in self.guests:
            print(guest)

    def list_reservations(self):
        for reservation in self.reservations:
            print(reservation)
