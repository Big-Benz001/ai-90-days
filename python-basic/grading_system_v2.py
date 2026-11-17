score = int(input("Enter your score: "))
if score < 0 or score > 100:
    print("Invalid score. Please enter a score between 0 and 100.")
elif score >= 70:
        print("Grade: A")
elif score >= 60:
        print("Grade: B")
elif score >= 50:
        print("Grade: C")
elif score >= 45:
        print("Grade: D")
else:
    print("Grade: F")