# вариант 1
# Известно, что X кг конфет стоит A рублей.
# Определить, сколько стоит 1 кг и Y кг этих же конфет.
while True:
    try:
        x = float(input("введите вес конфет в кг: "))
        a = float(input("введите стоимость конфет в рублях за 1 кг: "))
        y = float(input("введите вес для расчёта стоимости в кг: "))

        if x <= 0 or a <= 0 or y <= 0:
            print("Числа должны быть больше нуля или не равно нулю.")
            continue

        price_per_kg = a / x
        cost_y = price_per_kg * y

        print("стоимость 1 кг", price_per_kg,"руб.")
        print("стоимость y кг", cost_y,"руб.")
        break

    except ValueError:
        print("Ошибка! Вы ввели буквы вместо чисел.")
