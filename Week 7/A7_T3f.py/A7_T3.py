WEEKDAYS: tuple[str, ...] = (
"Monday",
"Tuesday",
"Wednesday",
"Thursday",
"Friday",
"Saturday",
"Sunday"
)

import os

def readFile(PFilename: str, PRows: list[str]) -> None:
    print(f'Reading file "{PFilename}".')
    PRows.clear()

    base_path = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(base_path, PFilename)
    print("Full path:", full_path)

    with open(PFilename, "r", encoding="UTF-8") as f:
        next(f)

        for line in f:
            if line.strip():
                PRows.append(line.strip())

    return None
   
def analyseTimestamps(PRows: list[str], PResults: list[str]) -> None:
    print("Analysing timestamps.")
    PResults.clear()
    weekday_counts: list[int] = [0] * len(WEEKDAYS)

    for PRow in PRows:
        for i, day in enumerate(WEEKDAYS):
            if PRow.startswith(day):
                weekday_counts[i] += 1

    PResults.append("### Timestamp analysis ###")

    return None


def displayResults(PResults: list[str]) -> None:
    print("Displaying results.")
    for line in PResults:
        print(line)
    

def main():
    print("Program starting.")
    PRows: list[str] = []
    PResults: list[str] = []

    PFilename = input("Insert filename: ")
    readFile(PFilename, PRows)
    analyseTimestamps(PRows, PResults)
    displayResults(PResults)
    print("Program ending.")

main()