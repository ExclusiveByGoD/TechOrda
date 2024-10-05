m = int(input())
s = list(map(int, input().strip('[]').split(',')))

price_to_indices = {}
found = False

for idx, price in enumerate(s):
    complement = m - price
    if complement in price_to_indices:
        indices = sorted([price_to_indices[complement], idx])
        print(f"{indices[0]} {indices[1]}")
        found = True
        break
    if price not in price_to_indices:
        price_to_indices[price] = idx

if not found:
    print("Не удалось найти подходящие акции.")
