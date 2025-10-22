# Create a program which prompts the user to insert an integer and then display the collatz conjecture as shown in the examples below.

print("Program starting.")
Integer = int(input("Insert a positive integer: "))

if Integer > 0:
    steps = 0
    print(str(Integer), end="")

    while Integer != 1:
        if Integer % 2 == 0:
            Integer = Integer // 2
        else:
            Integer = 3 * Integer + 1
        print(" -> " + str(Integer), end="")
        steps += 1

    print("\nSequence had " + str(steps) + " total steps.\n")

print("Program ending.")
