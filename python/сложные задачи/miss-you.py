array1 = list(map(int, input().strip('[]').split(',')))
array2 = list(map(int, input().strip('[]').split(',')))

set1 = set(array1)
missing_numbers = sorted(set(x for x in array2 if x not in set1))
print(missing_numbers)
