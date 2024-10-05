def my_min(arr):
    if not arr:
        return 0
    for i in range(len(arr)):
        if i == 0:
            min = arr[i]
        if arr[i] < min:
            min = arr[i]
    return min

a = list(map(int, input("Введите числа через пробел: ").split()))
print(my_min(a))