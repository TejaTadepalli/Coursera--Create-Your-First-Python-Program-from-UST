user_input = "random"
data = []

def show_menu():
    print("Menu")
    print("1. Add an Item")
    print("2. Mark as Done")
    print("3. View Items")
    print("4. Exit")


while user_input != "4":
    show_menu()
    user_input = input("Enter your choice: ")
    
    if user_input == "1":
        item = input("What is to be done? ")
        data.append(item)
        print("Item added: ", item)
    elif user_input == "2":
        item = input("What is to be marked as done? ")
        if item in data:
            data.remove(item)
            print("Removed Item: ", item)
        else:
            print("Item not found: ", item)
    elif user_input == "3":
        print("View the To-Do Items")
        for item in data:
            print(item)
    elif user_input == "4":
        print("Goodbye!")
    else:
        print("Invalid choice")