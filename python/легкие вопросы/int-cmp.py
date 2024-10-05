a = int(input("a = "))
b = int(input("b = "))

def int_cmp(a, b):
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0

print(int_cmp(a, b))