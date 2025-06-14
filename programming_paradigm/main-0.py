from bank_account import BankAccount
import sys

if len(sys.argv) > 1 and sys.argv[1] == "display":
    account = BankAccount()
    print(f"Current Balance: ${account.get_balance()}")
else:
    print("Usage: python main-0.py display")
