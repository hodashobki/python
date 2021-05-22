from bank_account import bank_account

class User:
    def __init__(self, name ,email):
        self. name=name
        self. email=email
        self. account=BankAccount()
    def make_deposit(self,amount):  
        self.account=+ amount 
        return self  
    def make_withdrawal(self,amount):
        self. account-= amount
        return self
    def display_user(self):
        print(self.name,self.account)
        return self
    def example_method(self):
        self.account.deposit(100)		# we can call the BankAccount instance's methods
        print(self.account.balance)		    
    
    def transfer_money(self, other_user,amount):
        self.account-=amount
        self.other_user=+amount 
        return self 
Hoda=User("hoda","dffas@ljh.com")
Ahmad=User("Ahmad","Ahmadd@gmail.com")
Laila=User("Laila","laila@gmail.com")
Hoda.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(50).display_user()
Laila.make_deposit(200).make_deposit(1200).make_withdrawal(400).make_withdrawal(100).display_user()
Ahmad.make_deposit(900).make_withdrawal(100).make_withdrawal(50).make_withdrawal(50)
Ahmad.display_user()

 