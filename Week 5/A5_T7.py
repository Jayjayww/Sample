DELIMITER = ","

def collectWords():
    words = []
    while True:
        word = input("Insert word(empty stops): ")
        if word == "":
            break
        words.append(word)
    return DELIMITER.join(words)

def analyseWords(words):
    word_list = words.split(DELIMITER)
    word_count = len(word_list)
    char_count = sum(len(w) for w in word_list)
    avg_length = char_count / word_count if word_count > 0 else 0

    print("-", word_count, "Words")
    print("-", char_count, "Characters")
    print("- {:.2f} Average word length".format(avg_length))     


def main():
    print("Program starting.")
    words = collectWords()
    analyseWords(words)
    print("Program ending.")


main()