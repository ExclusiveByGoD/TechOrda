def calc_deposit(n, k, b):
    for _ in range(n):
        b += b * (k / 100)
    return b

n = int(input("n = "))
k = float(input("k = "))
b = int(input("b = "))
print(calc_deposit(n, k, b))
