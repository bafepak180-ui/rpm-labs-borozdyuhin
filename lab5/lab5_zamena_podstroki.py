# Лабораторная работа №5, вариант 3
# Замена подстроки a -> b с подсчётом количества замен

text = input("Введите строку: ")
a = input("Что заменить: ")
b = input("На что заменить: ")
mode = input("Учитывать регистр? (да/нет): ").strip().lower()

if a == "":
    # пустую подстроку заменять нельзя — иначе зациклимся
    print("Пустая подстрока — заменять нечего")
else:
    # для поиска без учёта регистра сравниваем в нижнем регистре
    if mode == "нет":
        haystack = text.lower()
        needle = a.lower()
    else:
        haystack = text
        needle = a

    # проходим по строке и вручную собираем результат, считая замены
    result = ""
    count = 0
    i = 0
    while i < len(text):
        if haystack.startswith(needle, i):
            result += b
            count += 1
            i += len(a)
        else:
            result += text[i]
            i += 1

    print("Результат:", result)
    print("Количество замен:", count)
