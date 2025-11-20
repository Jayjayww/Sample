# Create a program that copies a text file by reading from a source file and writing the content to a destination file. Allow the user to specify the source and destination file names.

def main():
    print("Program starting.")
    print("This program can copy a file.")

    source_file = input("Insert source filename: ")
    destination_file = input("Insert destination filename: ")

    print(f"Reading file '{source_file}' content.")

    with open(source_file, "r", encoding="UTF-8") as src:
            content = src.read()
    print("File content ready in memory.")

    print(f"Writing content into file '{destination_file}'.")
    with open(destination_file, "r", encoding="UTF-8") as dest:
        dest.write(content)
    print("Copying operation complete.")

    print("Program ending.")

if __name__ == "__main__":
    main()