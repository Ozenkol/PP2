class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def withdraw(self, withdraw):
        if withdraw > self.balance:
            print(f"Недостаточно средств для списния, {self.owner} попробуйте выбрать другую сумму")
        else:
            self.balance = self.balance - withdraw
            print(f"Операция прошла успешна\nОстаток на вашем балансе равна {self.balance}")

    def deposite(self, deposite):
        self.withdraw(deposite)






a = Account("Temirlan", 65000)
a.withdraw(1)
