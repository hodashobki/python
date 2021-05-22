class BankAccount:
    def __init__(self, name,email ):
        self.name=name
        self.email=name
        self.account = BankAccount(int_rate=0.02, balance=0)
        # self.account_balance=0

    def deposit(self, amount):
        self.balance+=amount
        return self  
    def withdraw(self, amount):
        if self.balance >amount:
            self.balance-=amount
        else:
            print("insufficient funds:charging a $5 fee")
            self.balance-=5  
        return self      
    def display_account_info(self):
        print(self.balance)
        return self
    def yield_interest(self):
        if self.balance>0:
            self.balance +=( self.balance*self.int_rate)
            return self
Account_1=BankAccount(0.12,2500)
Account_1.deposit(1000). withdraw(200).yield_interest().display_account_info() 
Account_2=BankAccount(0.13,4500)
Account_2.deposit(200).deposit(205).deposit(1000).withdraw(450).display_account_info()
Account_3=BankAccount(0.09,250)
Account_3.deposit(1000).deposit(500).withdraw(100).withdraw(100).withdraw(200).withdraw(50).display_account_info()

		