# Ввести N чисел. Найти и вывести их среднее арифметическое.
n = input("Введите количество чисел : ")
while type(n) != int:
    try:
        n = int(n)
        if n <= 0:
            print("Количество чисел должно быть больше 0!")
    except ValueError:
        print("Введён неккоректный символ . Попробуйте снова")

total_sum = 0
i = 1

while i <= n:
    num = input(f"Введите {i}-е число: ")
    while type(num) != float:
        try:
            num = float(num)
        except ValueError:
            print("Неправильно ввели! Введите число.")
            num = input(f"Введите {i}-е число: ")

    total_sum += num
    i += 1

a = total_sum / n
print("Среднее арифметическое:", a)
