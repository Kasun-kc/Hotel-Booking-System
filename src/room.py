class Room:
    def __init__(self, room_id, room_type, price, status="Available"):
        self.room_id = room_id
        self.room_type = room_type
        self.price = price
        self.status = status

    def __str__(self):
        return f"Room {self.room_id}: {self.room_type}, ${self.price}, {self.status}"
