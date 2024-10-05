num = int(input("Введите число: "))
if num > 1:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print("Число не является простым.")
            break
    else:
        print("Число является простым.")
else:
    print("Число не является простым.")
