#Create a Python program to convert Fahrenheit to Celcius. Round the Celsius to 1 decimal precision.

#Formula to calculate Celcius from Fahrenheit is (Fahrenheit - 32) / 1.8

print("Program starting.")
Fahrenheit = float(input("Insert fahrenheits: "))
Celcius = float((Fahrenheit - 32) / 1.8)
print(f"{Fahrenheit}°F is {Celcius}°C")
print("Program ending.")