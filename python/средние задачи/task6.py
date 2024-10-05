import math

num = 25

def is_perfect_square(x):
    s = int(math.isqrt(x))
    return s * s == x

def is_fibonacci(n):
    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)

if is_fibonacci(num):
    print(f"{num} является числом Фибоначчи.")
else:
    print(f"{num} не является числом Фибоначчи.")
