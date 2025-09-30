print("Program starting")
print("Insert two integers")
int1 = int(input("Insert first integer: "))
int2 = int(input("Insert second integer: "))

print("Comparing inserted integers")
if int1 == int2:
    print("Integers are the same")
elif int1 > int2:
    print("First integer in greater")
elif int1 < int2:
    print("Second integer is greater")

total = int1 + int2
print("\nAdding integers together")
print(f"{int1} + {int2} = {total}")

print("\nChecking the parity of the sum...")
if total % 2==0:
    print("Sum is even")
else:
    print("Sum is odd")
print("Program ending.")