a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

def max_of_three(a, b, c):
    if a > b and a > c: 
        return a
    elif b > a and b > c:
        return b
    else:
        return c
    
print(max_of_three(a, b, c))