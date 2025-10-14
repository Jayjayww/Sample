# Create a program which prompts the user to insert an integer and then display the collatz conjecture as shown in the examples below.

print("Program starting.")
Integer = int(input("Insert a positive integer: "))
sequence = Integer
while Integer != 1:
    if Integer % 2 == 0:
        Integer //= 2
    else:
        Integer = 3 * Integer + 1
print(" -> ".join(map(str, sequence)))
print(f"Sequence had {len(sequence) - 1} total steps.\n")
