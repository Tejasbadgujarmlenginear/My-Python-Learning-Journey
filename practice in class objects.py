#create account class with 2 attributes - balance and account no .
#create method for debit, credit and printing the balance

class Account():

    def __init__(self,bal,acc_no):
        self.balance = bal
        self.account_num = acc_no
     
    #debit balance
    def debit(self,amount):
        self.balance -= amount
        print("rs",amount,"was debited")
        print("total balance",self.get_balance())

    #credit balance    
    def credit(self,amount):
        self.balance += amount
        print("Rs",amount,"was credite") 
        print("total balance",self.get_balance())

    #balance
    def get_balance(self):
        return self.balance      


acc1 = Account(100000,12345672)
acc1.debit(15000)
acc1.credit(1500)
acc1.credit(500000)
acc1.debit(86500)
