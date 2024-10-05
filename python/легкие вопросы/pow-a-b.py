a = int(input("a = "))
b = int(input("b = "))

def pow_a_b(a, b):
    res = 1
    for i in range(b):
        res *= a
    return res

print(pow_a_b(a, b))