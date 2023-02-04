class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        self.deposites = 0


    def withdraw(self, withdraw):
        if withdraw > self.balance:
            print(f"Недостаточно средств для списния, {self.owner} попробуйте выбрать другую сумму")
        else:
            self.balance = self.balance - withdraw
            print(f"Операция прошла успешна\nОстаток на вашем балансе равна {self.balance}")

    def deposite(self, deposite):
        if deposite > self.balance:
            print(f"Недостаточно средств для списния, {self.owner} попробуйте выбрать другую сумму")
        else:
            self.balance = self.balance - deposite
            self.deposites = self.deposites + deposite
            print(f"Операция прошла успешна\nОстаток на вашем депозите равна {self.deposites}")


a = Account("Temirlan", 65000)
a.withdraw(1)
a.deposite(1)
a.deposite(2)
a.withdraw(90000)
