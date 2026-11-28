# Дан список A размера N и целые числа K и L (1 < K < L < N).
# Переставить в обратном порядке элементы списка, расположенные
# между элементами AK и AL, не включая эти элементы.
import random
n = int(input("Введите размер списка : "))
k = int(input("Введите K: "))
l = int(input("Введите L: "))
list_a = []
for i in range(n):
    list_a.append(random.randint(0, 1000))
list_a[k : l - 1] = list_a[k : l - 1][::-1]
print("Исходный список: ", list_a)
print("Результирующий список: ", list_a)

