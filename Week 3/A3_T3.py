# Create a program with a plain menu.

# Prompt username first
# Make program menu with following options:
# Print welcome message
# Welcome {Name}!
# Exit
# Exiting...
# Prompt user to choose option “Your choice:”
# Perform actions based on the user input
# Creating menus like this is a really handy way to make tiny text-based programs and there will be more exercises like this in the future.

# The expectation at this point is that the user is able to choose option by inserting corresponding number. No error handling is required, it will be introduced later.

# Other possible output variats:

print("Program starting.")
name = input("This is a program with simple menu, where you can choose which operation the program performs. Before the menu, please insert your name: ")

while True:
    print("\nOptions:")
    print("1 - Print welcome message")
    print("0 - Exit")
    choice = input("Your choice: ")
    
    if choice == "0":
        print("Exiting...")
        break
    elif choice == "1":
        print(f"Welcome {name}!")
        break
    else:
        print("Unknown option.")  

print("\nProgram ending.")
