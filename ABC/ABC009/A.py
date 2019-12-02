N = int(input())
product = int(N / 2)
reminder = int(N % 2)
print(product + reminder)

# 別解
N = int(input())
print((N + 1) // 2)