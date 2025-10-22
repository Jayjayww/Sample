# Make Python program which prompts user to insert two integers. Use these integers together with the “while-loop” structure to create behaviour like in the example program run below.

# Note! the autograding tool will test that the correct structure has been applied.

print("Program starting.")

starting_value = int(input("Instert starting value: "))
stopping_value = int(input("Insert stopping value: "))

if starting_value <= stopping_value:
    i = starting_value
    while i <= stopping_value:
        print(i)
        i += 1
else:
    i = starting_value
    while i >= stopping_value:
        print(i)
        i -= 1

print("\nProgram ending.")