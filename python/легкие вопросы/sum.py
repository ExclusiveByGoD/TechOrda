def my_sum(array):
    sum = 0
    for i in array:
        sum += i
    return sum

a = list(map(int, input("Введите числа через пробел: ").split()))
print(my_sum(a))