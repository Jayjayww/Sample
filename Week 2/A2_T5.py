#Make a Python program, which prompts for a compound word.

# 1. Get following aspects from the word
#   1. Length
#   2. First character
#   3. Reversed version e.g. “Suitcase” is reversed “esactiuS”
# 2. Display the aspects using print commands.
# 3. Prompt the user to take substring from the existing compound word.
# 4. Finally print the user specified substring.

print("Program starting.\n")
word = input("Inser a closed compound word: ")
print("The word you inserted is", f"'{word}'" ",and in reverse it is ", f"'{word[::-1]}'" ".")
print("The inserter word leght is", len(word))
print("Last character is", f"'{word[-1]}'" ".")

print("\nTake a substring from the inserted word by inserting...")
start = int(input("Starting point (0 - {}): ".format(len(word)-1)))
end = int(input("Ending point ({} - {}): ".format(start, len(word))))
step = int(input("Step size (1 - {}): ".format(len(word)-start)))
print("1) Starting point:", start)
print("2) Ending point:", end)
print("3) Step size:", step )

print(f"\nThe word '{word}' sliced to the defined substring is '{word[start:end:step]}'")
print("Program ending.")