def main():
    print("Program starting.")
    print("This program analyses a list of names from a file.")

    filename = input("Insert a filename to read: ")

    print(f"Reading names from '{filename}'.")

    with open(filename, "r", encoding="UTF-8") as f:
        names = [line.strip() for line in f if line.strip()]
        print("Analysing names ...")
        count = len(names)

        shortest = len(min(names, key = len)) if count > 0 else 0
        longest = len(max(names, key = len)) if count > 0 else 0
        average = (sum(len(n) for n in names) / count ) if count > 0 else 0.0

        print("Analysis complete.")

    report = ("### REPORT BEGIN ###\n"
              f"Name count - {count}\n"
              f"Shortest name - {shortest}\n"
              f"Longest name - {longest}\n"
              f"Average name - {average}\n"
              "### REPORT END ###"
              )
    
    print(report)
    print("Program ending.")

if __name__ == "__main__":
    main()