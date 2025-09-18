#Make a Python program, which prompts the user name and two floating numbers.
#Multiply the inserted numbers to get product. Round the product in two decimal precision. 
#Complete the program output as shown below.

print("Program starting.")
name = input("What is your name: ")
float1 = input("Enter a floating point number: ")
float2 = input("Enter second floating point number: ")
print( name + " you gave numbers " + float1 + " and " + float2)
print("Multiplying first and second number will result in product " + str(float(float1) * float(float2)))
print("Program ending.")