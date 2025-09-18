#Prompt the user to insert the minutes spent on each previous topic task. 
#Calculate the sum and the average. Display those in the example program run format(Note! precision). 
#Make sure to calculate the required average for two decimal digits and later integer as rounded integer (precision 0 + type conversion).

print("Program starting.")
print("Estimate how many minutes you spent on programming...\n")

A1_T1 = int(input("A1_T1:"))
A1_T2 = int(input("A1_T2:"))
A1_T3 = int(input("A1_T3:"))
A1_T4 = int(input("A1_T4:"))
A1_T5 = int(input("A1_T5:"))
A1_T6 = int(input("A1_T6:"))
A1_T7 = int(input("A1_T7:"))

print("\nIn total you spent", int(A1_T1 + A1_T2 + A1_T3 + A1_T4 + A1_T5 + A1_T6 + A1_T7), "minutes on programming.")
print("Average per task was",  round((A1_T1 + A1_T2 + A1_T3 + A1_T4 + A1_T5 + A1_T6 + A1_T7) / 7, 2), "min and same rounded to nearest integer is", round((A1_T1 + A1_T2 + A1_T3 + A1_T4 + A1_T5 + A1_T6 + A1_T7) / 7, 0), "min.\n")
print("Program ending.")