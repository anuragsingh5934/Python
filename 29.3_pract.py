class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    def debit(self, amount):
        self.balance =- amount
        print("Rs.", amount , "was credited")
        print('Total balance = ' , self.get_balance())
    
    def get_balance(self):
        return self.balance

acc1 = Account(1000, 12345)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(100_000)