# main-function
# Print starting and ending statements.
# Print any empty row (see example program run)
# Prompt user to insert a word.
# Pass the inserted word into the frameWord-function.
# Returns None
# frameWord
# Takes PWord as a parameter.
# Prints the framing and the PWord
# Hint: Multiply the asterisk '*'-character.
# Returns None
# Note! Tests for this task relies on properly defined functions and may fail if the program is not written according to the instructions.

def frameWord(pword) -> None:
    lenght = len(pword) + 4
    print("*" * lenght)
    print(f"* {pword} *")
    print("*" * lenght)
    return None

def main() -> None:
    print("Program staring.")
    pword = input("Insert word: ")
    print()
    frameWord(pword)
    print()
    print("Program ending.")
    return None

main()

