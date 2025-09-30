# Prompt user to insert value as an integer.
# Display menu
# option 1 - In one multi-branched decision
# option 2 - Independent if-statement decisions
# option 0 - Exit
# Prompt user to choose option
# Apply following math operations in the options 1 & 2
# One multi-branched decision structure:
# Value is 400 or more => add 44 to the existing value
# Value is 200 or more => add 22 to the existing value
# Value is 100 or more => add 11 to the existing value
# Independent if-statement decisions one after another:
# Value is 400 or more => add 44 to the existing value
# Value is 200 or more => add 22 to the existing value
# Value is 100 or more => add 11 to the existing value
# Exit: “Exiting…”
# At the end of the options 1 & 2, show the results like in the example program runs.
# Other possible output variats:

# “Unknown option.”

print("Program starting.")
print("Testing decision structures.")
int1 = int(input("Insert an integer: "))
print("\nOptions:")
print("1 - In one multi-branched decision")
print("2 - In multiple independent if-statements")
print("0 - Exit")
choice = input("Your choice: ")

if choice == "1":
    print("Using one multi-branched decision structure.")
    if int1 >= 400:
        result = int1 + 44
        print(f"Result is {result}")

    elif int1 >= 200:
        result = int1 + 22
        print(f"Result is {result}")

    elif int1 >= 100:
        result = int1 + 11
        print(f"Result is {result}")

elif choice == "2":
    print("Using multiple independent if-statements structure.")
    if int1 >= 400:
        result = int1 + 44 + 22 + 11
        print(f"Result is {result}")
    elif int1 >= 200:
        result = int1 + 22 + 11
        print(f"Result is {result}")
    elif int1 >= 100:
        result = int1 + 11
        print(f"Result is {result}")

elif choice == "0":
    print("Exiting...")
else:
    print("Unknown options")

print("Program ending.")