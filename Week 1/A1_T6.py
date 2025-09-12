#Create a Python program that is able to calculate remainder. Remainder can be calculated using modulo “%” operator.

# 1. Prompt user “Insert an integer: ” and assign the input value into Feed variable
feed = input("Insert an integer: ")

# 2. Convert the Feed into an integer and assign it to Value variable
value = int(feed)

# 3. Calculate the remainder of the Value when divided by 2 and assign it to the Remainder variable.
remainder = value % 2

# 4. Print the inserted value “Value is {Value}”
print(f"Value is {value}")

# 5. Print the remainder value “The remainder is {Remainder} when {Value} is divided by 2.”
print(f"The remainder is {remainder} when {value} is divided by 2.")