from hotel import Hotel
from room import Room
from guest import Guest
from reservation import Reservation

def main():
    hotel = Hotel("Hotel Booking System")
    while True:
        print("\nHotel Booking System")
        print("1. Add Room")
        print("2. Add Guest")
        print("3. Make Reservation")
        print("4. Cancel Reservation")
        print("5. List Rooms")
        print("6. List Guests")
        print("7. List Reservations")
        print("8. Exit")
        
        print("--------------------------------------------------------------------------")
        
        choice = input("Enter your choice: ")

        print("--------------------------------------------------------------------------")

        if choice == "1":
            room_id = int(input("Enter Room ID: "))
            room_type = input("Enter Room Type (Single/Double/Suite): ")
            price = float(input("Enter Room Price: "))
            hotel.add_room(Room(room_id, room_type, price))
            print("--------------------------------------------------------------------------")
            print("Room added successfully!")
            print("--------------------------------------------------------------------------")

        elif choice == "2":
            guest_id = int(input("Enter Guest ID: "))
            name = input("Enter Guest Name: ")
            contact_details = input("Enter Contact Details: ")
            hotel.add_guest(Guest(guest_id, name, contact_details))
            print("--------------------------------------------------------------------------")
            print("Guest added successfully!")
            print("--------------------------------------------------------------------------")

        elif choice == "3":
            reservation_id = int(input("Enter Reservation ID: "))
            guest_id = int(input("Enter Guest ID for Reservation: "))
            room_id = int(input("Enter Room ID for Reservation: "))
            check_in_date = input("Enter Check-In Date (YYYY-MM-DD): ")
            check_out_date = input("Enter Check-Out Date (YYYY-MM-DD): ")

            guest = next((g for g in hotel.guests if g.guest_id == guest_id), None)
            room = next((r for r in hotel.rooms if r.room_id == room_id), None)

            if guest and room:
                hotel.make_reservation(Reservation(reservation_id, guest, room, check_in_date, check_out_date))
            else:
                print("--------------------------------------------------------------------------")
                print("Guest or Room not found!")
                print("--------------------------------------------------------------------------")

        elif choice == "4":
            reservation_id = int(input("Enter Reservation ID to Cancel: "))
            hotel.cancel_reservation(reservation_id)

        elif choice == "5":
            print("--------------------------------------------------------------------------")
            print("\nRooms:")
            hotel.list_rooms()

        elif choice == "6":
            print("--------------------------------------------------------------------------")
            print("\nGuests:")
            hotel.list_guests()

        elif choice == "7":
            print("--------------------------------------------------------------------------")
            print("\nReservations:")
            hotel.list_reservations()

        elif choice == "8":
            print("--------------------------------------------------------------------------")
            print("Exiting the system. Goodbye!")
            print("--------------------------------------------------------------------------")
            break

        else:
            print("--------------------------------------------------------------------------")
            print("Invalid choice! Please try again.")
            print("--------------------------------------------------------------------------")

if __name__ == "__main__":
    main()
