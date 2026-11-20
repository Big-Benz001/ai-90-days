def add (a, b):
    return a + b

def checker(a):
    if a % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
total = 0
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in list1:
    total += num
print(total)
print(f"The Sum is: {total}")
average = total / len(list1)
print(f"The Average is: {average}")

numbers = [12, 45, 3, 89, 22, 7]
print(f"The Maximum is: {max(numbers)}")
print(f"The Minimum is: {min(numbers)}")

names = ["Alice", "Bob", "Charlie", "David"]
for name in names:
    print(name)

student1 = {"name": "Alice", 
            "age": 20, 
            "course": "Computer Science",
            "scores": {"maths": 90, "english": 85, "science": 95}}
scores = student1["scores"].values()
average = sum(scores)/ len(scores)
print(f"The Average Score is: {average}")

list2 = [1, 2, 3, 3, 4, 5]
set1 = set(list2)
print(set1)

list3 = [1, 2, 3, 4, 5]
list4 = [4, 5, 6, 7, 1]
common_elements = set(list3).intersection(set(list4))
print(common_elements)

numbers2 = [1, 2, 3, 4, 5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
squared_numbers = [num ** 2 for num in numbers2]
print(squared_numbers)

words = ["hello", "world", "python", "programming"]
long_words = [word for word in words if len(word) > 5]
print(long_words)