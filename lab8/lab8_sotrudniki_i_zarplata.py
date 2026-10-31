# Лабораторная работа №8, вариант 3
# Тема: наследование, полиморфизм, интерфейсы
# Сотрудники: Employee -> Manager, Developer, Designer; расчёт зарплаты

from abc import ABC, abstractmethod


# Абстрактный базовый класс: общее имя, ставка и обязательный метод salary
class Employee(ABC):
    def __init__(self, name, base):
        self.name = name
        self.base = base

    @abstractmethod
    def salary(self):
        pass

    def info(self):
        return f"{self.name}: {self.salary():.2f} руб."


# Наследник 1: менеджер получает ставку плюс премию
class Manager(Employee):
    def __init__(self, name, base, bonus):
        super().__init__(name, base)
        self.bonus = bonus

    def salary(self):
        return self.base + self.bonus


# Наследник 2: разработчику платят за переработанные часы
class Developer(Employee):
    def __init__(self, name, base, hours):
        super().__init__(name, base)
        self.hours = hours

    def salary(self):
        return self.base + self.hours * 500


# Наследник 3: дизайнеру доплачивают за проекты
class Designer(Employee):
    def __init__(self, name, base, projects):
        super().__init__(name, base)
        self.projects = projects

    def salary(self):
        return self.base + self.projects * 3000


# Ввод числа с защитой от букв и пустой строки
def read_number(text):
    while True:
        try:
            return float(input(text))
        except ValueError:
            print("Нужно число, попробуйте снова")


def main():
    base = read_number("Базовая ставка: ")

    # Общий список объектов базового типа — полиморфизм
    staff = [
        Manager("Иванов", base, 15000),
        Developer("Петров", base, 40),
        Designer("Сидорова", base, 3),
    ]

    total = 0
    for emp in staff:
        print(emp.info())
        total += emp.salary()

    print(f"Фонд оплаты труда: {total:.2f} руб.")


main()
