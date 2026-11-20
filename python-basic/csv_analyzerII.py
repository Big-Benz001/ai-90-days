
import csv

# Initialize dictionaries and counters
department_salary = {}
department_count = {}
department_average = {}

emp = 0
invalid_records = 0

try:
    with open("employees.csv", "r") as file:
        reader = csv.DictReader(file)

        # STEP 1: Read and process employee records
        for i in reader:
            emp += 1

            department = i["Department"]

            # STEP 2: Validate employee salary
            try:
                salary = int(i["Salary"])

            except ValueError:
                print(f"Invalid salary for {i['Name']}")
                invalid_records += 1
                continue

            # STEP 3: Calculate total salary per department
            if department in department_salary:
                department_salary[department] += salary
            else:
                department_salary[department] = salary

            # STEP 4: Count employees per department
            if department in department_count:
                department_count[department] += 1
            else:
                department_count[department] = 1

        # STEP 5: Check whether the CSV is empty
        if emp == 0:
            print("Empty File")

        else:
            # STEP 6: Calculate department averages
            for department, total in department_salary.items():
                count = department_count[department]
                average = total / count
                department_average[department] = average

            # STEP 7: Display department report
            print("\n========== DEPARTMENT REPORT ==========")

            for department, total in department_salary.items():
                print(f"{department}: Total Salary = ₦{total:,}")

            for department, count in department_count.items():
                print(f"{department}: Employees = {count}")

            for department, average in department_average.items():
                print(f"{department}: Average Salary = ₦{average:,.2f}")

            # STEP 8: Display overall statistics
            valid_employees = sum(department_count.values())
            total_salary = sum(department_salary.values())

            print("\n========== OVERALL SUMMARY ==========")
            print(f"Total Records Read: {emp}")
            print(f"Valid Employees: {valid_employees}")
            print(f"Invalid Records: {invalid_records}")
            print(f"Total Salary: ₦{total_salary:,}")

            if valid_employees > 0:
                overall_average = total_salary / valid_employees
                print(f"Overall Average Salary: ₦{overall_average:,.2f}")

except FileNotFoundError:
    print("File not found.")

except PermissionError:
    print("You do not have permission to access this file.")
