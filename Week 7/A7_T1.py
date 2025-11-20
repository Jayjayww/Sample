def int_collector():
    numbers: list[int] = []
    while True:
        try:
            integer = int(input("Insert positive integer(negative stops): "))
        except ValueError:
            print("Invalid input")
        if integer < 0:
            break
        elif integer > 0:
            numbers.append(integer)
        else:
            print("0 is not valid! Enter postive integer(negative stops.)")

    print("Stopped collecting positive integers.")

    if numbers:
        print(f"Displaying {len(numbers)} integers: ")
        for index, integer in enumerate(numbers):
            ordinal = index + 1
            print(f"- Index {index} => Ordinal {ordinal} => Integer {integer}")
    else:
        print("No integers to display.")

def main():
    print("Program starting.")
    print("Collect positive integers.")
    int_collector()
    print("Program ending.")


if __name__ == "__main__":
    main()