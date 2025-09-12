# Create a Python program that is able to calculate car’s fuel consumption (diesel or petrol) and present the consumption in liters per 100km “x l per 100 km”

# 1. Print info message “Calculate fuel consumtion.”
print("Calculate fuel consumption.")

# 2. Ask “Enter travel distance(kilometers): ” and store the value to Feed variable
feed = input("Enter travel distance(kilometers): ")

# 3. Convert the Feed into an integer and assign it to Distance variable
distance = int(feed)

# 4. Ask “Enter fuel usage(liters): ”
feed = input("Enter fuel usage(liters): ")

# 5. Convert the Feed into an integer and assign it to FuelUsage variable
fuelUsage = int(feed)

# 6. Calculate the Consumption for 100 km
# Consumption = (FuelUsage / Distance) * 100

# 7. Convert the Consumption back to an integer
consumption = (fuelUsage / distance) * 100

# 8. Print “Fuel consumption is {Consumption} l per 100 km”
print("Fuel consumption is " + str(consumption) + " l per 100 km")