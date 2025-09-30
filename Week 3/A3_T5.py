# Create a temperature unit conversion program.

# Start the program by listing options for the user:

# Celsius to Fahrenheit
# Fahrenheit to Celsius
# Exit
# Prompt user to insert choice. After the decision to convert, ask the amount of current temperature (use the floating point datatype). Lastly show the converted value to the user.

# For the unit conversions, use the formula Celsius = (Fahrenheit - 32) / 1.8

# Data representation examples:

# 50.0 °F
# 10.0 °C
# Use 1 decimal precision to round the converted value.

print("Program starting.")
print("\nOptions:")
print("1 - Celsius to Fahrenheit")
print("2 - Fahrenheit to celsius")
print("0 - Exit")
choice = int(input("Your choice: "))
                   
if choice == 1:
    celcius = float(input("Insert the amount of Celcius: "))
    fahrenheit = celcius * 1.8 + 32
    print(f"{round(celcius, 1)} °C equals to {round(fahrenheit, 1)} °F")

elif choice == 2:
    fahrenheit = float(input("Insert the amount of Fahrenheit: "))
    celcius = (fahrenheit - 32) / 1.8
    print(f"{round(fahrenheit, 1)} °F equals to {round(celcius, 1)} °C")
elif choice == 0:
    print("Exiting...")
else:
    print("Unknown option.")
print("")
print("Program ending.")