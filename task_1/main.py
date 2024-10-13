class InsufficientFundsError(Exception):
    def __str__(self):
        return 'Недостаточно средств!'


class BankAccount:
    def __init__(self, amount: int):
        self.balance = amount

    def deposit(self, amount: int):
        if amount <= 0:
            raise ValueError('Баланс меньше нуля')
        self.balance += amount

    def withdraw(self, amount: int):
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise InsufficientFundsError

    def get_balance(self):
        return self.balance


if __name__ == '__main__':
    a1 = BankAccount(1000)