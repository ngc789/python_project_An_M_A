while True:
    try:
        x = float(input("введите координату X: "))

        y = float(input("Введите координату Y: "))
        if x > 0 and y > 0:
            print("1 четверть")
        elif x < 0 and y > 0:
            print("2 четверть")
        elif x < 0 and y < 0:
            print("3 четверть")
        elif x > 0 and y < 0:
            print("4 четверть")

    except ValueError:
        print("введён некоректный символ! попробуйте снова.")

