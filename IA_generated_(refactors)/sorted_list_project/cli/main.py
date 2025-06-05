from sorted_list.sorted_list import SortedList

def run_cli():
    sl = SortedList()
    while True:
        choice = input("Enter a number, 's' to show, or 'q' to quit: ").strip().lower()
        if choice == 'q':
            print("Goodbye.")
            break
        elif choice == 's':
            sl.display()
        else:
            try:
                value = int(choice)
                sl.add(value)
                print(f"Added {value}.")
            except ValueError:
                print("Invalid input. Enter an integer, 's', or 'q'.")
