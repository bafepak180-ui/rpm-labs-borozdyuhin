# Лабораторная работа №7, вариант 3
# Класс BankAccount: номер, владелец, баланс; пополнение, снятие, перевод


class BankAccount:
    def __init__(self, number, owner, balance=0):
        self._number = number
        self._owner = owner
        self._balance = balance

    # доступ к приватным полям через свойства
    @property
    def number(self):
        return self._number

    @property
    def owner(self):
        return self._owner

    @property
    def balance(self):
        return self._balance

    # пополнение счёта
    def deposit(self, amount):
        if amount <= 0:
            print("Сумма пополнения должна быть больше нуля")
            return False
        self._balance += amount
        print(f"{self._owner}: пополнение на {amount}, баланс {self._balance}")
        return True

    # снятие со счёта
    def withdraw(self, amount):
        if amount <= 0:
            print("Сумма снятия должна быть больше нуля")
            return False
        if amount > self._balance:
            print(f"{self._owner}: недостаточно средств (баланс {self._balance})")
            return False
        self._balance -= amount
        print(f"{self._owner}: снятие {amount}, баланс {self._balance}")
        return True

    # перевод на другой счёт
    def transfer(self, other, amount):
        if amount <= 0:
            print("Сумма перевода должна быть больше нуля")
            return False
        if amount > self._balance:
            print(f"{self._owner}: недостаточно средств для перевода")
            return False
        self._balance -= amount
        other.deposit(amount)
        print(f"Перевод {amount} от {self._owner} к {other.owner}")
        return True

    def show(self):
        print(f"Счёт {self._number}: {self._owner}, баланс {self._balance}")


# чтение суммы с клавиатуры с проверкой
def read_amount(text):
    try:
        return float(input(text))
    except ValueError:
        print("Нужно ввести число")
        return 0


def main():
    acc1 = BankAccount("001", "Иванов", 1000)
    acc2 = BankAccount("002", "Петров", 500)
    acc3 = BankAccount("003", "Сидоров")

    print("--- Все счета ---")
    for acc in (acc1, acc2, acc3):
        acc.show()

    print("--- Пополнение ---")
    acc3.deposit(300)

    print("--- Снятие ---")
    acc1.withdraw(200)
    acc1.withdraw(5000)

    print("--- Перевод ---")
    acc2.transfer(acc3, 150)

    print("--- Итог ---")
    for acc in (acc1, acc2, acc3):
        acc.show()

    # пополнение счёта суммой, введённой с клавиатуры
    amount = read_amount("Сумма для пополнения счёта 001: ")
    acc1.deposit(amount)
    acc1.show()


main()
