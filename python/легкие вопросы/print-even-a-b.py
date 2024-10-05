a = int(input("a = "))
b = int(input("b = "))

def print_even_a_b(a, b):
    l = []
    for i in range(a, b + 1):
        if i % 2 == 0:
            l.append(i)
    return l

print(print_even_a_b(a, b))