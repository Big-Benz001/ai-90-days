import json 
employee = {
    "name": "Abdulkareem",
    "age": 25,
    "department": "Technology",
    "skills": ["Python","HTML","CSS"]
}
employee_data = json.dumps(employee)

print(employee_data)
print(type (employee_data))

employee_object = json.loads(employee_data)

print(employee_object)
print(type(employee_object))