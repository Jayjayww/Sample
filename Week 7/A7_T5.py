import csv
from datetime import datetime
from collections import defaultdict

def read_csv(filename):
    weekdays = []
    consumptions = []
    prices = []

    with open(filename, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=";")

        for row in reader:
            weekdays.append(row["Weekday"])
            consumptions.append(float(row["Consumption(kWh)"]))
            prices.append(float(row["Price(€/kWh)"]))

    return weekdays, consumptions, prices

def analyse_daily_usage(weekdays, consumptions, prices):
    day_usage = defaultdict(float)
    day_cost = defaultdict(float)

    for day, usage, price in zip(weekdays, consumptions, prices):
        day_usage[day] += usage
        day_cost[day] += usage * price

    return day_usage, day_cost

def display_results(day_usage, day_cost):
    days = [
        "Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"
    ]

    print("### Electricity consumption summary ###")
    for day in days:
        usage = day_usage.get(day, 0.0)
        cost = day_cost.get(day, 0.0)
        print(f"-{day} usage {usage:.2f} kWh, cost {cost:.2f} €")
    print("### Electricity consumption summary ###")

import os

def main():
    print("Program starting.")
    filename = input("Insert filename: ")

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(BASE_DIR, "A7_T5 Folder", filename)

    print(f'Reading file "{filepath}".')
    weekdays, consumptions, prices = read_csv(filepath)

    print("Analysing timestamps.")
    day_usage, day_cost = analyse_daily_usage(
        weekdays, consumptions, prices
    )

    print("Displaying results.")
    display_results(day_usage, day_cost)

    print("Program ending.")

if __name__ == "__main__":
    main()