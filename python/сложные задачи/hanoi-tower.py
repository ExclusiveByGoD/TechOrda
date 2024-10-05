def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Диск {n} с башни {source} переложить в башню {target}")
    else:
        hanoi(n - 1, source, auxiliary, target)
        print(f"Диск {n} с башни {source} переложить в башню {target}")
        hanoi(n - 1, auxiliary, target, source)

n = int(input())
hanoi(n, 1, 3, 2)
