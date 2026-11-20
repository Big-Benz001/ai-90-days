with open("my_profile.txt","w") as file:
    file.write("Shonibare Abdulkareem\n")
    file.write("Occupation: Software Engineer\n")
    file.write("Favorite Programming Language: Python\n")
    file.write("Current Goal: To become a senior AI engineer\n")

with open("my_profile.txt","r") as file:
    content = file.read()
    print(content)

with open("my_profile.txt","a") as file:
    file.write("Additional Information: i am commited to becoming an iai engineer\n")

with open("my_profile.txt","r") as file:
    content = file.read()
    print(content)