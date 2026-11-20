import json

employee = {
    "name": "Abdulkareem",
    "age": 25,
    "department": "Technology",
    "skills": ["Python","HTML","CSS"]
}

with open("employee.json", "w") as file :
    json.dump(employee,file, indent = 4 )

with open ("employee.json","r") as doc:
    employee_data = json.load(doc)
print(employee_data)
print(type(employee_data))
