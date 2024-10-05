def my_sort(array):
    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array

a = list(map(int, input("Введите числа через пробел: ").split()))
print(my_sort(a))