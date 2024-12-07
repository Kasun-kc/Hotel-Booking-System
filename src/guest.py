class Guest:
    def __init__(self, guest_id, name, contact_details):
        self.guest_id = guest_id
        self.name = name
        self.contact_details = contact_details

    def __str__(self):
        return f"Guest {self.guest_id}: {self.name}, {self.contact_details}"
