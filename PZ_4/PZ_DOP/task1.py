# Ввести 4 числа. Найти и вывести на экран сумму
# и количество отрицательных чисел.
a,b,c,d = (input("Введите 1 число: "),
           input("Введите 2 число: "),
           input("Введите 3 число: "),
           input("Введите 4 число: "))
while type(a) != float:
    try:
        a = float(a)
    except ValueError:
        print("Введён неккоректный символ . Попробуйте снова")
        a = input("Введите 1 число: ")
while type(b) != float:
    try:
        b = float(b)
    except ValueError:
        print("Введён неккоректный символ . Попробуйте снова")
        b = input("Введите 2 число: ")

while type(c) != float:
    try:
        c = float(c)
    except ValueError:
        print("Введён неккоректный символ . Попробуйте снова")
        c = input("Введите 3 число: ")

while type(d) != float:
    try:
        d = float(d)
    except ValueError:
        print("Введён неккоректный символ . Попробуйте снова")
        d = input("Введите 4 число: ")
sum_neg = 0
total_neg = 0

for x in (a,b,c,d):
    if x < 0:
        sum_neg += 1
        total_neg += 1
print("Количество отрицательных чисел:", total_neg)
print("Сумма отрицательных чисел:", sum_neg)

