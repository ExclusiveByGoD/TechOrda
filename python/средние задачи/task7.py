num = int(input("Введите число: "))
divisors_sum = sum(i for i in range(1, num) if num % i == 0)
if num == divisors_sum:
    print(f"{num} является совершенным числом.")
else:
    print(f"{num} не является совершенным числом.")
