from core.hotel_message_system import HotelMessageSystem

def run_cli():
    system = HotelMessageSystem()

    while True:
        print('\nHotel Message System CLI')
        print('1. Leave a message for a guest')
        print('2. Check messages for yourself')
        print('3. Exit')
        choice = input('Choose an option (1/2/3): ').strip()

        if choice == '1':
            guest_name = input('Enter guest\'s full name: ').strip()
            last_name = guest_name.split()[-1]
            message = input('Enter the message: ').strip()
            system.add_message(last_name, guest_name, message)
            print(f'Message left for {guest_name}.')

        elif choice == '2':
            guest_name = input('Enter your full name: ').strip()
            last_name = guest_name.split()[-1]
            messages = system.get_messages(last_name, guest_name)
            if messages:
                print(f'\nMessages for {guest_name}:')
                for idx, msg in enumerate(messages, 1):
                    print(f'{idx}. {msg}')
                system.remove_messages(last_name, guest_name)
                print('All messages retrieved and removed from the system.')
            else:
                print('No messages found for you.')

        elif choice == '3':
            print('Exiting Hotel Message System.')
            break
        else:
            print('Invalid option. Please choose 1, 2, or 3.')
