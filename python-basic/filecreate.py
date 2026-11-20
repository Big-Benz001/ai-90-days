import csv
empolyees = [
    ["name", "age", "department", "salary"],
    ["John", 25, "IT", 150000],
    ["Sarah", 28, "HR", 120000],
    ["Mike", 30, "Finance", 200000],
    ["David", 32, "Marketing", 140000],
    ["Grace", 26, "IT", 180000],
]

with open ("employees.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(empolyees)
    print("CSV file created successfully.")

with open ("employees.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

with open ("employees.csv", "r") as doc:
    reader = csv.DictReader(doc)
    for row in reader:
        print(row["name"])
        print(row["department"])
        print(row["salary"])