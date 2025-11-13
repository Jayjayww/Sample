LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def shiftCharacter(ch, alphabet):
    if ch in alphabet:
        return alphabet[(alphabet.index(ch) + 13) % 26]
    else:
        return ch

def rot13(text):
    return ''.join(
        shiftCharacter(ch, LOWER_ALPHABETS) if ch.islower() else
        shiftCharacter(ch, UPPER_ALPHABETS) if ch.isupper() else
        ch
        for ch in text
    )

def writeFile(filename, lines):
    with open(filename, "w", encoding="UTF-8") as f:
        f.write(''.join(lines))


def main():
    print("Program starting.\n")
    print("Collecting plain text rows for ciphering.")
    rows = []

    while True:
        row = input("Insert row (empty stops): ")
        if row == "":
            break
        rows.append(row)

    ciphered_rows = [rot13(row) for row in rows]

    print("\n#### Ciphered text ####")
    for line in ciphered_rows:
        print(line)

    choice = input("Insert filename to save (empty = skip): ")
    if choice:
        writeFile(choice, ciphered_rows)
        print("Ciphered text saved!")
    else:
        print("Ciphered text not saved.")

    print("Program ending.")


if __name__ == "__main__":
    main()
