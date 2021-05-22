class User:
    def __init__(self, name ,email):
        self. name=name
        self. email=email
        self. account_balance=0
    def make_deposit(self,amount): 
        self.account_balance+=amount 
        return self  
    def make_withdrawal(self,amount):
        self. account_balance-= amount
        return self
    def display_user(self):
        print(self.name,self.account_balance)
        return self
    
    def transfer_money(self, other_user,amount):
        self.account_balance=-amount
        self.other_user=+amount 
        return self 
Hoda=User("Hoda","hoda@lgmail.com")
Laila=User("Laila","laila@gmail.com")
Ahmad=User("Ahmad","Ahmadd@gmail.com")

Hoda.make_deposit(200)
Hoda.make_deposit(200)
Hoda.make_withdrawal(300)  
Hoda.display_user()

Laila.make_deposit(200)
Laila.make_deposit(1200)
Laila.make_withdrawal(400)
Laila.make_withdrawal(100)
Laila.display_user()


Ahmad.make_deposit(900)
Ahmad.make_withdrawal(100)
Ahmad.make_withdrawal(50)
Ahmad.make_withdrawal(50)
Ahmad.display_user()



