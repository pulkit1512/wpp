class bank:
    def __init__(self,name,account_number,balance):
        self.name=name
        self.__account_number=account_number
        self.balance=balance
    def get_account_number(self):
        return f"your account nuimber is :{self.__account_number}"
    def display_balance(self):
        return f"your bank balance is:{self.balance}"
    def deposit(self,amount):
         self.balance += amount 
         return f"the updated bank balance is :{self.balance}"
    
    def withdraw(self,amount):
        if (amount>self.balance):
            return "Insufficient balance"
        else:
            self.balance-=amount
            return f"the remaininng bank balance is {self.balance}"
   
pulkit=bank("pulkit",123456789,10000) 
print(pulkit.get_account_number())
print(pulkit.display_balance())
print(pulkit.deposit(1000))
print(pulkit.withdraw(5000))
print(pulkit.display_balance())       
print(pulkit.withdraw(15000))
      
       