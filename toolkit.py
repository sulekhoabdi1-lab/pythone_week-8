# Personal Mini-Toolkit Main Program

def number_guessing_game():
    """Tool 1: A number guessing game with hints and attempt tracking."""
    print("\n--- Number Guessing Game ---")
    secret_number = 4
    attempts = 0
   
    while True:
        try:
            guess = int(input("Guess a number between 1 and 10: "))
            attempts += 1
            if guess == secret_number:
                print(f"🎉 Congratulations! You guessed it in {attempts} attempts.")
                break
            elif guess < secret_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        except ValueError:
            print("Please enter a valid number.")

def shopping_list_manager():
    """Tool 2: A dynamic shopping list manager using lists and loops."""
    print("\n--- Quick Shopping List Manager ---")
    my_list = []
   
    while True:
        print("\nList Menu: [1] Show [2] Add [3] Remove [4] Back to Main Menu")
        choice = input("Choose an option (1-4): ").strip()
       
        if choice == "1":
            if not my_list:
                print("Your shopping list is empty.")
            else:
                print("Current Shopping List:")
                for index, item in enumerate(my_list, start=1):
                    print(f"{index}. {item}")
        elif choice == "2":
            item = input("Enter item to add: ").strip()
            if item:
                my_list.append(item)
                print(f"'{item}' has been added.")
        elif choice == "3":
            item = input("Enter item to remove: ").strip()
            if item in my_list:
                my_list.remove(item)
                print(f"'{item}' has been removed.")
            else:
                print("That item is not on your list.")
        elif choice == "4":
            print("Returning to Main Menu...")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")

def countdown_timer():
    """Tool 3: A countdown timer using a while loop."""
    print("\n--- Countdown Timer ---")
    try:
        start = int(input("Enter a number to count down from: "))
        if start <= 0:
            print("Please enter a number greater than 0.")
            return
       
        while start > 0:
            print(start)
            start -= 1
        print("🚀 Blast off! Countdown complete.")
    except ValueError:
        print("Please enter a valid integer.")

def main():
    print("👋 Welcome to your Personal Mini-Toolkit!")
   
    while True:
        print("\n==============================")
        print("     PERSONAL MINI-TOOLKIT    ")
        print("==============================")
        print("1. Number Guessing Game")
        print("2. Quick Shopping List")
        print("3. Countdown Timer")
        print("4. Quit")
       
        choice = input("Enter your choice (1-4): ").strip()
       
        if choice == "1":
            number_guessing_game()
        elif choice == "2":
            shopping_list_manager()
        elif choice == "3":
            countdown_timer()
        elif choice == "4":
            print("\n🌟 Thank you for using Personal Mini-Toolkit. Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please select an option between 1 and 4.")

if __name__ == "__main__":
    main()
