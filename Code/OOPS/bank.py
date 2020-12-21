""" using basic OOPS concept for normal-bank debit & credit """

class BankAccount:
    def __init__(self,owner,balance=0.0):
        self.owner=owner
        self.balance=balance
        
    def deposit(self,credit):
        self.balance+=credit
        return self.balance
        
    def withdraw(self,debit):
        self.balance-=debit
        return self.balance


user1=BankAccount("Jijo",25)
user2=BankAccount("Snehal",27)
print(user1.owner,user1.balance)
print(user1.deposit(15)) 