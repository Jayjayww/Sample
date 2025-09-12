# Make a Python program which can take user inputs and convert them into integers.

# 1. Print “Calculate the area of a wall.”
print("Calculate the area of a wall.")

# 2. Prompt user
    # 1. “Enter the width in meters: ”
    # 2. Store the input value into Feed variable.
feed = input("Enter the width in meters" )

# 3. Convert the Feed variable into an integer and store it in Width variable
width = float(feed)

# 4. Prompt user
    # 1. “Enter the height in meters: ”
    # 2. store the input value into Feed variable.
feed = input("Enter the height in meters: ")

# 5. Convert the Feed variable into an integer and store it in Height variable
height = float(feed)

# 6. Print “Width is {Width} m and height is {Height} m.”
print(f"Width is {width} m and height is {height} m.")

# 7. Multiply Width and Height, then store the result in Area variable
area = width * height

# 8. Display results to the user: “The wall will be {Area} square meters.”
print("The wall will be " + str(area) + " square meters.")