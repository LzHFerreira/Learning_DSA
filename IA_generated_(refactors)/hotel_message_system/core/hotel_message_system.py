def get_last_name_key(last_name):
    return last_name.strip()[0].upper()

class HotelMessageSystem:
    def __init__(self):
        self.slots = {chr(i): [] for i in range(ord('A'), ord('Z') + 1)}

    def add_message(self, last_name, guest_name, message):
        key = get_last_name_key(last_name)
        self.slots[key].append((guest_name, message))

    def get_messages(self, last_name, guest_name):
        key = get_last_name_key(last_name)
        messages = [msg for name, msg in self.slots[key] if name.lower() == guest_name.lower()]
        return messages

    def remove_messages(self, last_name, guest_name):
        key = get_last_name_key(last_name)
        self.slots[key] = [item for item in self.slots[key] if item[0].lower() != guest_name.lower()]
