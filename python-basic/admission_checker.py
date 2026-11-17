applicant_age = int(input("Enter your age: "))
is_olevel_credit = input("Do you have O'level credit? (yes/no): ")
if applicant_age >= 16:
    if is_olevel_credit == "yes":
        print("You are eligible for admission.")
    else:
        print("O'level credit is required for admission.")
else:
    print("You do not meet the age requirement for admission.")