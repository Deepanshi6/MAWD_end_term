#from pydantic import BaseModel
#Internet wasn't allowed so I couldn't install pydantic
from typing import Optional
'''
class Bank(BaseModel):
    account_number:int
    account_holder:str
    balance:Optional[int]=0
    '''
class BankAccount(account_n=int , account_h=str , balance=int):
    def __init__(self,account_n,account_h,b):
        self.account_number=account_n
        self.account_holder=account_h
        self.balance=b

    def display_info(self,account_number,account_holder,b):
        print("Account Number :",self.account_n)
        print("Account Holder :",self.account_h)
        print("balance :",self.balance)

    def deposit(self,b,amount=int):
        self.balance+=amount
        print("Balance now :",self.balance)

    def withdraw(self,b,amount=int):
        self.balance-=amount
        print("Balance now :",self.balance)

B1=BankAccount(1,"Dee",100000)
B2=BankAccount(2,"Abc",2000)
B1.display_info()
B2.display_info()
B1.deposit(10)
B2.deposit(200)
B1.withdraw(5)
B2.withdraw(10)

#partial marks