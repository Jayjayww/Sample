# Create a program that can write a text file. Prompt the user to insert first name and last name. Then prompt the file name for the write operation. Finally write a text file with first name on the first row and last name on the second row. Ensure that the text file ends in a empty row. Finally exit the program cleanly.



def main():
    try:
        first_name = input("Insert first name: ")
        last_name = input("Insert last name: ")
        file_name = input("Insert filename: ")
        if not file_name.endswith(".txt"):
            file_name += ".txt"

        with open(file_name, "w") as file:
            file.write(f"{first_name}\n")
            file.write(f"{last_name}\n")
            file.write("\n")

            print("Program ending.")

    except Exception as e:
        print(f"An error occured: {e}")

if __name__ == "__main__":
    main()