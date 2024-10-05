def my_range(n):
    arr = []
    for i in range(1, n+1):
        arr.append(i)
    return arr

if __name__ == "__main__":
    print(my_range(int(input())))