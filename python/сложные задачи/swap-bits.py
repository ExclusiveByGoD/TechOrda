a = int(input())
result = ((a & 0x0F) << 4) | ((a & 0xF0) >> 4)
print(result)
