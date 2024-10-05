array = list(map(int, input().strip('[]').split(',')))
total_sum = sum(array)
left_sum = 0

for num in array:
    total_sum -= num
    if left_sum == total_sum:
        print('true')
        break
    left_sum += num
else:
    print('false')
