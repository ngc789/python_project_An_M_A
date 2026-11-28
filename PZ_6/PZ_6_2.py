# Дан список размера N. Найти номера тех элементов списка, которые
# больше своего правого соседа, и количество таких элементов.
# Найденные номера выводить в порядке их возрастания.
import random
n = int(input("Введите размер списка: "))
numbers_full = []
for i in range(n):
    numbers_full.append(random.randint(0,100))

big_numbers = []
for i in range(n - 1):
    if numbers_full[i] > numbers_full[i + 1]:
        big_numbers.append(i+1)
print("Исходный список: ", numbers_full)
print("Номера элементов, больших правого соседа: ", big_numbers)
print("Количество таких элементов: ", len(big_numbers))

