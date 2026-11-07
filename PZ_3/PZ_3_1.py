while True:
    try:
        a = int(input("Введите число: "))

        if a > 0:
            print("Число положительное")
        else:
            print("Число отрицательное")
        continue

    except ValueError:
        print("Введено не число! Попробуйте снова")