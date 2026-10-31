# Лабораторная работа №3, вариант 3
# Тема: циклические алгоритмы
# Задание: вывести все простые числа от 1 до N

# ввод N с проверкой (do-while: повторяем, пока не введут нормальное число)
while True:
    text = input("Введите N: ")
    try:
        n = int(text)
    except ValueError:
        print("Это не целое число, попробуйте ещё раз")
        continue
    if n < 1:
        print("N должно быть не меньше 1")
        continue
    break

# поиск простых чисел: внешний while по числам, внутренний for по делителям
primes = []
number = 2
while number <= n:
    is_prime = True
    for d in range(2, int(number ** 0.5) + 1):
        if number % d == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(number)
    number += 1

# вывод результата
if primes:
    print("Простые числа от 1 до", n, ":", *primes)
    print("Всего:", len(primes))
else:
    print("Простых чисел от 1 до", n, "нет")
