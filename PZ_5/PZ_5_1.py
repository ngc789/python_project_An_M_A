# 1. Составить функцию решения задачи: из заданного числа вычли сумму его цифр.
# Из результата вновь вычли сумму его цифр и т. д.
# Через сколько таких действий получится нуль?
def sums(summ_number):
    total = 0
    while summ_number > 0:
        total += summ_number % 10
        summ_number //= 10
    return total
def calc(subt):
    subtraction = 0
    while subt > 0:
        subt -= sums(subt)
        subtraction += 1
    return subtraction
while True:
    try:
        us_number = int(input("Введите число деляющиеся нацело: "))
        if us_number < 0:
            print("Число должно быть больше нуля")
            continue
        break
    except ValueError:
        print("Введён неккоретный символ или цифра не деляющиеся нацело . Попробуйте снова ")


result = calc(us_number)
print("Результат",result)



