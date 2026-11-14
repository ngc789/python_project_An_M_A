# Найти и вывести на экран S = 1! + 2! + 3! + 4! + ... + n! (n > 1).
n = input("Введите целое число : ")
while type(n) != int:
    try:
        n = int(n)
        if n <= 1:
            print("Число должно быть больше 1!")
    except ValueError:
        print("Введён неккоректный символ . Попробуйте снова")

f = 1
total_sum = 0

for i in range(1, n + 1):
    f *= i
    total_sum += f

print("Сумма S =", total_sum)