class Bank():
    def __init__(self, account, money):
        self.money = money
        self.account = account

    def balance(self):
        return self.money
    
    def owner(self):
        return self.account
    
    def deposit(self, money):
        self.money+=money

        return f"You are deposit {money} money"
    
    def withdraw(self, money2):
        if self.money - money2 < 0:
            return "insufficient funds"
        else:
            self.money-=money2

            return f"you're balance: {self.money},  and you take {money2}"
        
        
bank = Bank("Bekzat", 1000)

print(bank.balance())

print(bank.owner())

print(bank.deposit(1000))

print(bank.withdraw(3000))

print(bank.withdraw(2000))