# Лабораторная работа №9, вариант 3
# Подсчёт строк, слов и символов в файле и копирование файла

import os


# своё исключение для ошибок данных
class EmptyFileError(Exception):
    pass


def make_demo(path):
    # создаём демонстрационный файл, если нужного нет
    with open(path, "w", encoding="utf-8") as f:
        f.write("Первая строка текста\n")
        f.write("Вторая строка тоже здесь\n")
        f.write("Третья и последняя\n")


def count_text(path):
    # считаем строки, слова и символы
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    if text.strip() == "":
        raise EmptyFileError("файл пустой, считать нечего")
    return len(text.splitlines()), len(text.split()), len(text)


def copy_file(src, dst):
    # копируем файл построчно
    with open(src, "r", encoding="utf-8") as fin, open(dst, "w", encoding="utf-8") as fout:
        for line in fin:
            fout.write(line)


def main():
    src = "data.txt"
    dst = "copy.txt"

    # если файла нет — создаём демонстрационный
    if not os.path.exists(src):
        make_demo(src)
        print("Файл", src, "не найден, создан демонстрационный.")

    try:
        lines, words, chars = count_text(src)
        copy_file(src, dst)
    except FileNotFoundError:
        print("Ошибка: файл не найден")
        return
    except PermissionError:
        print("Ошибка: нет доступа к файлу")
        return
    except OSError as e:
        print("Ошибка ввода-вывода:", e)
        return
    except EmptyFileError as e:
        print("Ошибка данных:", e)
        return

    print("Строк:", lines)
    print("Слов:", words)
    print("Символов:", chars)
    print("Копия сохранена в", dst)

    # сколько первых строк показать
    try:
        n = int(input("Сколько первых строк показать? "))
    except (ValueError, EOFError):
        n = 3
    with open(dst, "r", encoding="utf-8") as f:
        for i, line in enumerate(f):
            if i >= n:
                break
            print(line.rstrip())


main()
