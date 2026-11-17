# Basic Arithmetic Operations in Python
a = 50
b = 20
c = a + b
d = a - b
e = a * b
f = a / b
print(f"Addition: {c}")
print(f"Subtraction: {d}")
print(f"Product: {e}")
print(f"Quotient: {f}")

# Even or Odd
number = 17
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")

# Comparison 
age = 27
voting_age = 18
if age >= voting_age:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
# assignment operators
balance = 50000
balance += 10000  
balance -= 5000
balance *= 2
print(f"Final balance: {balance}")
# operator precedence
result = 10 + 5 * 2 ** 2
print(result)