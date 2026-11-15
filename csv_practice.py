#Python is able to make reading a CSV file easier. Excel is able to make the data easy to read. 
#A real business process that would benefit from an append-mode log file is if someone wanted to check the total data of something over time. 

import csv
from datetime import datetime

print("--Exercise 2--")
with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

print("--Exercise 3--")
with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader)
    print(header)

    for row in reader:
        print(row)

print("--Exercise 4--")
total_revenue = 0
with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader)
    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])
        total = price * quantity
        total_revenue = total_revenue + total

        print(f"{product}: {quantity} units x ${price:.2f} = ${total:.2f}")

print(f"Total revenue: ${total_revenue:.2f}")

print("--Exercise 5--")
original_count = 0
written_count = 0

with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader)
    with open("data/sales_copy.csv", "w", newline="") as new_file:
        writer = csv.writer(new_file)
        writer.writerow(["product", "price", "quantity", "total"])

        for row in reader:
            original_count = original_count + 1
            product = row[0]
            price = float(row[1])
            quantity = int(row[2])

            total = price * quantity
            if total > 100:
                writer.writerow([product, price, quantity, total])
                written_count = written_count + 1

print(f"Original count: {original_count}")
print(f"Written count: {written_count}")

print("--Exercise 6--")

dict_total = 0
with open("data/sales.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])
        total = price * quantity
        dict_total = dict_total + total

        print(f"{product}: ${total:.2f}")

print(f"Total revenue: ${dict_total:.2f}")

print("--Exercise 7--")

summary = {}

with open("data/sales.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])
        total = price * quantity

        if product in summary:
            summary[product] = summary[product] + total
        else:
            summary[product] = total

for product in sorted(summary):
    print(f"{product}: ${summary[product]:.2f}")