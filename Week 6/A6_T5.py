SEPARATOR = ";"


def readValues(filename: str) -> str:
    with open(filename, "r", encoding="UTF-8") as f:
        lines = f.readlines()

    values = ""
    for line in lines:
        number = line.strip()
        if number.isdigit():
            values += number + SEPARATOR

    return values.rstrip(SEPARATOR)


def analyseValues(values_str: str) -> str:
    numbers = [int(x) for x in values_str.split(SEPARATOR)]

    count = len(numbers)
    total = sum(numbers)
    greatest = max(numbers)
    average = total / count if count > 0 else 0

    header = f"Count{SEPARATOR}Sum{SEPARATOR}Greatest{SEPARATOR}Average"
    result_line = f"{count}{SEPARATOR}{total}{SEPARATOR}{greatest}{SEPARATOR}{average:.2f}"

    return f"{header}\n{result_line}\n"

def main():
    print("Program: starting.")
    filename = input("Insert filename: ")

    values_str = readValues(filename)
    analysis_str = analyseValues(values_str)

    print("### Number analysis - START ###")
    print(f'File "{filename}" results : ')
    print(analysis_str, end="")  # avoid double newlines
    print("### Number analysis - END ###")
    print("Program: ending.")


if __name__ == "__main__":
    main()