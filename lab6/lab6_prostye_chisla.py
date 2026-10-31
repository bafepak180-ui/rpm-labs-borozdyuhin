# Лабораторная работа №6, вариант 3
# Простые числа: IsPrime, NextPrime, PrimeRange


def read_number(prompt):
    """Читает целое число с клавиатуры, при ошибке просит ввести заново."""
    while True:
        text = input(prompt)
        try:
            return int(text)
        except ValueError:
            print("Ошибка: нужно целое число, попробуйте снова.")


def is_prime(n):
    """Проверяет, является ли число n простым."""
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def next_prime(n):
    """Возвращает ближайшее простое число, которое больше n."""
    candidate = n + 1
    while not is_prime(candidate):
        candidate += 1
    return candidate


def prime_range(start, end):
    """Возвращает список простых чисел из отрезка [start, end]."""
    result = []
    for number in range(start, end + 1):
        if is_prime(number):
            result.append(number)
    return result


def print_result(title, value):
    """Выводит подпись и результат на экран."""
    print(title, value)


def show_menu():
    """Печатает меню и возвращает выбранный пункт."""
    print("\n1 - проверить число на простоту")
    print("2 - найти следующее простое число")
    print("3 - вывести простые числа в диапазоне")
    print("0 - выход")
    return read_number("Выберите пункт: ")


def main():
    """Главный цикл программы: меню, обработка, вывод."""
    while True:
        choice = show_menu()

        if choice == 0:
            print("Работа завершена.")
            break
        elif choice == 1:
            number = read_number("Введите число: ")
            print_result("Число простое?", is_prime(number))
        elif choice == 2:
            number = read_number("Введите число: ")
            print_result("Следующее простое число:", next_prime(number))
        elif choice == 3:
            start = read_number("Начало диапазона: ")
            end = read_number("Конец диапазона: ")
            if start > end:
                print("Ошибка: начало больше конца.")
            else:
                print_result("Простые числа:", prime_range(start, end))
        else:
            print("Нет такого пункта меню.")


main()
