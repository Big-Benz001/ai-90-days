number = 10
if number > 1:
    for i in range(2, number):
        if number % i == 0:
            print(f"Number {number} is not prime.")
            break
    else:
        print(f"Number {number} is prime.")