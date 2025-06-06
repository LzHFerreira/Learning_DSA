# Simple hotel message system using a dictionary to simulate the dovecot cupboard.
# Messages are stored by the first letter of the guest's last name (A-Z).
# Interactive CLI for adding and retrieving messages.


def get_last_name_key(last_name):
    """
    Returns the uppercase first letter of the last name.
    Used as the key for the message slots.
    """
    return last_name.strip()[0].upper()


class HotelMessageSystem:
    def __init__(self):
        # Initialize slots for each letter A-Z, each slot is a list of messages
        self.slots = {chr(i): [] for i in range(ord("A"), ord("Z") + 1)}

    def add_message(self, last_name, guest_name, message):
        """
        Add a message for a guest.
        Args:
            last_name: The guest's last name.
            guest_name: The guest's full name.
            message: The message content.
        """
        key = get_last_name_key(last_name)  # Get the slot key (A-Z)
        # Store as a tuple (guest_name, message)
        self.slots[key].append((guest_name, message))

    def get_messages(self, last_name, guest_name):
        """
        Retrieve all messages for a guest with the given last name and full name.
        Args:
            last_name: The guest's last name.
            guest_name: The guest's full name.
        Returns:
            List of messages for the guest.
        """
        key = get_last_name_key(last_name)  # Get the slot key (A-Z)
        # Filter messages for the exact guest name
        messages = [
            msg for name, msg in self.slots[key] if name.lower() == guest_name.lower()
        ]
        return messages

    def remove_messages(self, last_name, guest_name):
        """
        Remove all messages for a guest after retrieval.
        Args:
            last_name: The guest's last name.
            guest_name: The guest's full name.
        """
        key = get_last_name_key(last_name)
        # Keep only messages not for this guest
        self.slots[key] = [
            item for item in self.slots[key] if item[0].lower() != guest_name.lower()
        ]


def main():
    system = HotelMessageSystem()  # Create the message system

    while True:
        print("\nHotel Message System CLI")
        print("1. Leave a message for a guest")
        print("2. Check messages for yourself")
        print("3. Exit")
        choice = input("Choose an option (1/2/3): ").strip()

        if choice == "1":
            # Add a message for a guest
            guest_name = input("Enter guest's full name: ").strip()
            last_name = guest_name.split()[-1]  # Assume last word is last name
            message = input("Enter the message: ").strip()
            system.add_message(last_name, guest_name, message)
            print(f"Message left for {guest_name}.")

        elif choice == "2":
            # Retrieve messages for a guest
            guest_name = input("Enter your full name: ").strip()
            last_name = guest_name.split()[-1]  # Assume last word is last name
            messages = system.get_messages(last_name, guest_name)
            if messages:
                print(f"\nMessages for {guest_name}:")
                for idx, msg in enumerate(messages, 1):
                    print(f"{idx}. {msg}")
                # Remove messages after retrieval
                system.remove_messages(last_name, guest_name)
                print("All messages retrieved and removed from the system.")
            else:
                print("No messages found for you.")

        elif choice == "3":
            print("Exiting Hotel Message System.")
            break
        else:
            print("Invalid option. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()
