from dataclasses import dataclass

@dataclass
class BankAccount:
    account_holder:str
    account_number:str
    balance:float = 0.0
    #def check_balance(self)->None:
      #print(f"Account Holder: {self.account_holder}, Your Current: {self.balance}")
    def display_details(self) -> None:
        def display_details(self) -> None:
         print(f"Account Holder: {self.account_holder}")
         print(f"Account Number: {self.account_number}")
         print(f"Account Balance: ₦{self.balance:,.2f}")
    def deposit(self,amount:float) -> None:
       if amount > 0 :
          self.balance += amount
          print("Successful Deposit")
          print (f"New Balanace: {self.balance}")
       else:
          print("Enter a valid Amount")

    def withdraw(self, amount: float) -> None:
       if amount <= 0:
        print("Enter a valid amount")
       elif amount > self.balance:
        print("Insufficient funds in the account")
       else:
        self.balance -= amount
        print("Successful Withdrawal")
        print(f"New Balance: ₦{self.balance:,.2f}")

account1 = BankAccount("John", "0987654321", 5000)
account1.display_details()
account1.deposit(5000)
account1.withdraw(5000)
account1.display_details()