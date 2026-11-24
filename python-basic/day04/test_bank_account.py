import unittest
from bank_account import BankAccount

class TestBancAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount(
            "John",
            "0987654321",
            5000
        )
    def test_deposit(self):
        self.account.deposit(2000)
        self.assertEqual(self.account.balance, 7000)
    def test_invalid_deposit(self):
        self.account.deposit(-500)
        self.assertEqual(self.account.balance, 5000)
    def test_withdraw(self):
        self.account.withdraw(2000)
        self.assertEqual(self.account.balance, 3000)
    def test_insufficient_funds(self):
        self.account.withdraw(6000)
        self.assertEqual(self.account.balance, 5000)
    def test_withdraw_entire_balance(self):
        self.account.withdraw(5000)
        self.assertEqual(self.account.balance, 0)
     
if __name__ == "__main__":
    unittest.main()