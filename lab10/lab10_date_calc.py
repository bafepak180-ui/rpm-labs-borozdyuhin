"""
Модуль: date_calc.py
Тема: Калькулятор дат — разность, прибавление дней, день недели.

ПАСПОРТ МОДУЛЯ
Назначение: модуль выполняет простые вычисления с календарными датами —
считает количество дней между двумя датами, прибавляет к дате заданное число
дней (в том числе отрицательное) и определяет день недели для указанной даты.
Модуль используется как из командной строки, так и как библиотека (импорт без
побочных эффектов: ввод-вывод находится только внутри main()).

Функции:
  parse_date(text) -> date — разбирает строку вида "дд.мм.гггг" в объект date;
  date_diff(first, second) -> int — модуль разности дат в днях;
  add_days(day, count) -> date — дата, сдвинутая на count дней;
  weekday_name(day) -> str — название дня недели на русском.

Вход: строки с датой в формате дд.мм.гггг, целое число дней, номер пункта меню.
Выход: целое число дней, дата в формате дд.мм.гггг, название дня недели.
Ограничения: поддерживаются только даты григорианского календаря от 1 года
до 9999 года; формат даты строго дд.мм.гггг; при неверном вводе выбрасывается
ValueError, который перехватывается в main() и печатается сообщением об ошибке.

РУКОВОДСТВО ПОЛЬЗОВАТЕЛЯ
Запуск: python date_calc.py (нужен Python 3, сторонние библиотеки не требуются).
После запуска программа печатает меню из трёх пунктов. Пункт 1 — разность дат:
нужно ввести две даты в формате дд.мм.гггг, программа выведет число дней между
ними (результат неотрицательный). Пункт 2 — прибавление дней: вводится дата и
целое число дней, выводится получившаяся дата. Пункт 3 — день недели: вводится
дата, выводится название дня недели. Пример: пункт 1, даты 01.01.2024 и
01.02.2024 — ответ 31 дн.; пункт 2, дата 28.02.2024 и 5 дней — ответ 04.03.2024;
пункт 3, дата 09.05.2025 — ответ пятница. При ошибке ввода (буквы вместо числа,
несуществующая дата, неверный формат) программа печатает сообщение "Ошибка
ввода" и завершается без трассировки. Тесты запускаются командой
python -m unittest date_calc.py.
"""

from datetime import date, timedelta
import unittest


# Разбор строки с датой в формате дд.мм.гггг
def parse_date(text):
    parts = text.strip().split('.')
    if len(parts) != 3:
        raise ValueError('нужен формат дд.мм.гггг')
    return date(int(parts[2]), int(parts[1]), int(parts[0]))


# Разность дат в днях (без знака)
def date_diff(first, second):
    return abs((second - first).days)


# Прибавление дней к дате
def add_days(day, count):
    return day + timedelta(days=count)


# Название дня недели
def weekday_name(day):
    names = ['понедельник', 'вторник', 'среда', 'четверг',
             'пятница', 'суббота', 'воскресенье']
    return names[day.weekday()]


# Основной сценарий: меню, ввод, обработка, вывод
def main():
    print('1 - разность дат, 2 - прибавить дни, 3 - день недели')
    choice = input('Пункт: ').strip()
    try:
        if choice == '1':
            first = parse_date(input('Первая дата (дд.мм.гггг): '))
            second = parse_date(input('Вторая дата (дд.мм.гггг): '))
            print('Разность:', date_diff(first, second), 'дн.')
        elif choice == '2':
            day = parse_date(input('Дата (дд.мм.гггг): '))
            count = int(input('Сколько дней прибавить: '))
            print('Результат:', add_days(day, count).strftime('%d.%m.%Y'))
        elif choice == '3':
            day = parse_date(input('Дата (дд.мм.гггг): '))
            print('День недели:', weekday_name(day))
        else:
            print('Нет такого пункта')
    except ValueError as error:
        print('Ошибка ввода:', error)


# Модульные тесты
class TestDateCalc(unittest.TestCase):

    def test_parse_date_ok(self):
        self.assertEqual(parse_date('15.03.2024'), date(2024, 3, 15))

    def test_parse_date_bad_format(self):
        with self.assertRaises(ValueError):
            parse_date('15-03-2024')

    def test_parse_date_bad_day(self):
        with self.assertRaises(ValueError):
            parse_date('31.02.2024')

    def test_parse_date_letters(self):
        with self.assertRaises(ValueError):
            parse_date('аб.вг.де')

    def test_diff_same_day(self):
        self.assertEqual(date_diff(date(2024, 1, 1), date(2024, 1, 1)), 0)

    def test_diff_usual(self):
        self.assertEqual(date_diff(date(2024, 1, 1), date(2024, 2, 1)), 31)

    def test_diff_order(self):
        self.assertEqual(date_diff(date(2024, 2, 1), date(2024, 1, 1)), 31)

    def test_diff_leap_year(self):
        self.assertEqual(date_diff(date(2024, 1, 1), date(2025, 1, 1)), 366)

    def test_add_days_usual(self):
        self.assertEqual(add_days(date(2024, 1, 1), 10), date(2024, 1, 11))

    def test_add_days_zero(self):
        self.assertEqual(add_days(date(2024, 5, 5), 0), date(2024, 5, 5))

    def test_add_days_negative(self):
        self.assertEqual(add_days(date(2024, 3, 1), -1), date(2024, 2, 29))

    def test_add_days_new_year(self):
        self.assertEqual(add_days(date(2024, 12, 31), 1), date(2025, 1, 1))

    def test_weekday_monday(self):
        self.assertEqual(weekday_name(date(2024, 1, 1)), 'понедельник')

    def test_weekday_sunday(self):
        self.assertEqual(weekday_name(date(2024, 1, 7)), 'воскресенье')


if __name__ == '__main__':
    main()
    unittest.main()
