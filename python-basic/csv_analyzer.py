import csv 

total_salary = 0
emp = 0
max_salary = None
min_salary = None
with open ("employees.csv","r") as file:
    reader = csv.DictReader(file)
    for i in reader:
        emp +=1
        salary = int(i["Salary"])
        
        if max_salary is None or salary > max_salary:
            max_employee = i["Name"]
            max_salary = salary
        if min_salary is None or salary < min_salary:
            min_employee = i["Name"]
            min_salary = salary
        total_salary += salary

if emp > 0:
    average = total_salary / emp
    print(f"Average Salary: ₦{average:,.0f}")
else:
    print("No employee records found.")

print(f"Total Employee: {emp:,}")
print(f"Total Salary: ₦{total_salary:,}")
print(f"Average Salary: ₦{average:,}")
print(f"Highest paid Staff: {max_employee}- ₦{max_salary,}")
print(f"Lowest paid Staff: {min_employee}- ₦{min_salary,}")

        