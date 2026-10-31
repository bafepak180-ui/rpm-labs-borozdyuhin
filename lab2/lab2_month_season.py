# Лабораторная работа №2, вариант 3
# По номеру месяца выводим время года и количество дней

# ввод номера месяца с проверкой на число
try:
    month = int(input("Введите номер месяца (1-12): "))
except ValueError:
    print("Ошибка: нужно ввести целое число")
else:
    # проверка диапазона и определение сезона
    if 1 <= month <= 12:
        if month in (12, 1, 2):
            season = "зима"
        elif month in (3, 4, 5):
            season = "весна"
        elif month in (6, 7, 8):
            season = "лето"
        else:
            season = "осень"

        # количество дней в месяце
        if month == 2:
            days = 28
        elif month in (4, 6, 9, 11):
            days = 30
        else:
            days = 31

        print("Время года:", season)
        print("Количество дней:", days)
    else:
        print("Ошибка: месяц должен быть от 1 до 12")
