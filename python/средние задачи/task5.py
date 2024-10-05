print("Совершенные числа в диапазоне от 0 до 1000:")
for num in range(1, 1001):
    divisors_sum = sum(i for i in range(1, num) if num % i == 0)
    if num == divisors_sum:
        print(num)
