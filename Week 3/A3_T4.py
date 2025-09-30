# Extend the previous menu program by adding three more options to the menu.

# Options:

# Print the name backwards
# Your name backwards is "{NameBackwards}"
# Print the first character
# The first character in name "{Name}" is "{FirstChar}"
# Show the amount of characters in the name
# There are {NameLength} characters in the name "{Name}"

print("Program starting.")
name = input("This is a program with simple menu, where you can choose which operation the program performs. Before the menu, please insert your name: ")

while True:
    print("\nOptions:")
    print("1 - Print welcome message")
    print("2 - Print the name backwards")
    print("3 - Print the first character")
    print("4 - Show amount of characters in the name")
    print("0 - Exit")
    choice = input("Your choice: ")
    
    if choice == "0":
        print("Exiting...")
        break
    elif choice == "1":
        print(f"Welcome {name}!")
        break
    elif choice == "2":
        print(f'Your name backwards is "{name[::-1]}".')
        
    elif choice == "3":
        print(f'The first character in name "{name}" is "{name[0]}"')
        
    elif choice == "4":
        print(f'There are, {len(name)} characters in the name "{name}"')
    else:
        print("Unknown option.")  

print("\nProgram ending.")