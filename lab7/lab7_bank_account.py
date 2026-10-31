# Лабораторная работа №7, вариант 3
# Класс BankAccount: номер, владелец, баланс; пополнение, снятие, перевод

class BankAccount:
    def __init__(self, number, owner, balance=0):
        self._number = number
        self._owner = owner
        self._balance = balance

    # свойства для доступа к приватным полям
    @property
    def number(self):
        return self._number

    @property
    def owner(self):
        return self._owner

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            print("Баланс не может быть отрицательным")
            return
        self._balance = value

    # пополнение счёта
    def deposit(self, amount):
        if amount <= 0:
            print("Сумма пополнения должна быть больше нуля")
            return False
        self.balance = self.balance + amount
        return True

    # снятие денег
    def withdraw(self, amount):
        if amount <= 0:
            print("Сумма снятия должна быть больше нуля")
            return False
        if amount > self.balance:
            print("Недостаточно средств на счёте", self.number)
            return False
        self.balance = self.balance - amount
        return True

    # перевод на другой счёт
    def transfer(self, other, amount):
        if self.withdraw(amount):
            other.deposit(amount)
            print("Перевод", amount, "руб. со счёта", self.number, "на счёт", other.number)
            return True
        return False

    def show(self):
        print("Счёт", self.number, "| владелец:", self.owner, "| баланс:", self.balance)


# ввод суммы с проверкой на число
def read_amount(text):
    try:
        return float(input(text))
    except ValueError:
        print("Нужно ввести число")
        return 0


def main():
    # создаём счета
    acc1 = BankAccount("1001", "Иванов", 5000)
    acc2 = BankAccount("1002", "Петров", 1200)
    acc3 = BankAccount("1003", "Сидорова", 0)

    print("--- Счета ---")
    for acc in (acc1, acc2, acc3):
        acc.show()

    # пополнение и снятие
    print("\n--- Пополнение и снятие ---")
    amount = read_amount("Сумма пополнения для счёта 1003: ")
    acc3.deposit(amount)
    amount = read_amount("Сумма снятия со счёта 1001: ")
    acc1.withdraw(amount)

    # перевод между счетами
    print("\n--- Перевод ---")
    amount = read_amount("Сумма перевода с 1001 на 1002: ")
    acc1.transfer(acc2, amount)

    # итоговые балансы
    print("\n--- Итоговые балансы ---")
    for acc in (acc1, acc2, acc3):
        acc.show()


main()
