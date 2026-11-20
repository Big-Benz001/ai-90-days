try :
   a = int(input("Enter First Number: "))
   b = int(input("Enter Second Number: "))
   c = a/b
except ValueError:
   print( "Enter a valid Number not Text")
except ZeroDivisionError:
   print("Enter a number not zero")
else:
   print(f"Divison Answer {c}")
finally:
   print ("Progam Division operation completed.")
   