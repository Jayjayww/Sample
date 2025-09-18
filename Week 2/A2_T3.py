#Make Python program, which prompts user to insert two words. 
# Print the length of each word and then compound them together. 
# Put single quotes around the compound word.

print("Program starting.")
word1 = input("Insert first word: ")
word2 = input("Insert second word: ")
print("1st word is", len(word1), "characters long.")
print("2nd word is", len(word2), "characters long.")
print("Words together makes one closed compound", compound := "'" + word1 + word2 + "'")
print("Program ending.")