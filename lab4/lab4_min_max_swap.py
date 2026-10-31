# Лабораторная работа №4, вариант 3
# Подсчёт положительных/отрицательных/нулей и обмен min <-> max

def read_number(text):
    while True:
        try:
            return int(input(text))
        except ValueError:
            print("Нужно целое число, попробуйте снова")

# ввод размера и элементов массива
n = read_number("Сколько элементов? ")
while n <= 0:
    n = read_number("Размер должен быть больше нуля: ")

arr = []
for i in range(n):
    arr.append(read_number("arr[" + str(i) + "] = "))

print("Исходный массив:", arr)

# подсчёт положительных, отрицательных и нулей
pos = neg = zero = 0
for x in arr:
    if x > 0:
        pos += 1
    elif x < 0:
        neg += 1
    else:
        zero += 1

print("Положительных:", pos)
print("Отрицательных:", neg)
print("Нулей:", zero)

# поиск индексов минимума и максимума
imin = 0
imax = 0
for i in range(1, n):
    if arr[i] < arr[imin]:
        imin = i
    if arr[i] > arr[imax]:
        imax = i

print("min =", arr[imin], "max =", arr[imax])

# обмен минимального и максимального элементов
arr[imin], arr[imax] = arr[imax], arr[imin]
print("После обмена:", arr)
