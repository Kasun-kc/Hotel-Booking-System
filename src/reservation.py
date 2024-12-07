class Reservation:
    def __init__(self, reservation_id, guest, room, check_in_date, check_out_date, status="Active"):
        self.reservation_id = reservation_id
        self.guest = guest
        self.room = room
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.status = status

    def __str__(self):
        return (f"Reservation {self.reservation_id}: Guest {self.guest.name}, Room {self.room.room_id}, "
                f"From {self.check_in_date} to {self.check_out_date}, Status: {self.status}")
