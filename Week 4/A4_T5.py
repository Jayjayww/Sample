# Make a program, which prompts user to insert three integers:

# Starting point
# Stopping point
# Inspection point
# Test the points with following rules(Note! testing order matters):

# Starting point must be less than stopping point
# "Starting point value must be less than the stopping point value."
# The inspection point must be within the range of the start and stop points.
# "Inspection value must be within the range of start and stop."
# If any rule above is broken, print the violation message(s) to the user and then skip the next part till the "Program ending." print.

# Run two for-loops like shown in the example program runs if none of the rules above are broken. Inside the loops, compare the inspection point to the current iteration. Use break and continue commands if the current iteration is same as the inspection point. Otherwise print the current iteration on the same line.

# Note! There must be no trailing space character at the end of any row.

print("Program starting.\n")

Starting_point = int(input("Insert starting point: "))
Stopping_point = int(input("Insert stopping point: "))
Inspection_point= int(input("Insert inspection point: "))

run = True

if Starting_point >= Stopping_point:
    print("Starting point value must be less than the stopping value.")
    run = False

if Starting_point > Inspection_point or Inspection_point > Stopping_point:
    print("Inspection value must be within the range of start and stop.")
    run = False

if run:
    print("First loop - inspection with break: ")
    for i in range(Starting_point, Stopping_point):
        if(i == Inspection_point):
            break
        else:
            print(i, end=" ")
    print("\nSecond loop - inspection with continue")
    for i in range(Starting_point, Stopping_point):
        if(i == Inspection_point):
            continue
        else:
            if(i == Stopping_point):
                print(i)
            else:
                print(i, end=" ")

print("\nProgram ending.")