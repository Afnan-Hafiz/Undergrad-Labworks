class BankAccount:
  def __init__(self, user_name, account, balance=0):
    self.user_name= user_name  #instance attribute
    self.account_type= account
    self.balance= balance
  def balance(self,balance):
    self.balance=balance


account1 = BankAccount("Bilbo", "Savings")
account1.balance= 15.75





print("=====================================")
print(f"User Name: {account1.user_name}")
print(f"Balance: {account1.balance}")
print(f"Account Type:", account1.account_type)
print("=====================================")
account2 = BankAccount("Frodo", "Business")
print(f"User Name: {account2.user_name}")
print(f"Balance: {account2.balance}")
print(f"Account Type: {account2.account_type}")
print("=====================================")
print(account1.balance)