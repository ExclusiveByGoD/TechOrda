array = list(map(int, input().strip('[]').split(',')))
array.sort()
index = (len(array) - 1) // 2
print(array[index])
