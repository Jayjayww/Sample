# Create menu program with submenus. Mainly for unit conversions. Use the values from the following table for unit conversions https://www.isa.org/getmedia/192f7bda-c77c-480a-8925-1a39787ed098/CCST-Conversions-document.pdf

# Menu options:

# Length
# Meters to kilometers
# Kilometers to meters
# Weight
# Grams to pounds
# Pounds to grams
# Exit
# “Exiting...”
# Handle all the data in floating point datatype. Remember to round every value in 1 digit precision right before displaying.

# Other possible prints:

# “Unknown option.”
# Example run - weight conversion 1

print("Program starting.")
print("Welcome to the unit converter program!")
print("Follow the menu instructions below.")


print("\nOptions:")
print("1 - Length")
print("2 - Weight")
print("0 - Exit")
choice = input("Your choice: ")

if choice == "1":
    print("\nLenght options:")
    print("1 - Meters to kilometers")
    print("2 - Kilometers to meters")
    print("0 - Exit")
    choice2 = input("Your choice: ")

    if choice2 == "1":
        meters = float(input("Insert meters: "))
        kilometers = meters / 1000
        print(f"{round(meters, 1)}m is {round(kilometers, 1)} km")
    elif choice2 == "2":
        kilometers = float(input("Insert kilometers: "))
        meters = kilometers * 1000
        print(f"{round(kilometers, 1)}km is {round(meters, 1)}m")
    elif choice2 == "0":
        print("Exiting...")
    else:
        print("Unknown option.")

elif (choice == "2"):
    print("\nWeight options:")
    print("1 - Grams to pounds")
    print("2 - Pounds to grams")
    print("0 - Exit")
    choice2 = input("Your choice: ")

    if choice2 == "1":
        grams = float(input("Insert grams: "))
        pounds = grams * 0.00220462
        print(f"{round(grams, 1)}g is {round(pounds, 1)}lb")
    elif choice2 == "2":
        pounds = float(input("Insert pounds: "))
        grams = pounds / 0.00220462
        print(f"{round(pounds, 1)}lb is {round(grams, 1)}g")
    elif choice2 == "0":
        print("Exiting...")
    else:
        print("Unknown option.")
elif choice == "0":
    print("\nExiting...")

print("Program ending.")
