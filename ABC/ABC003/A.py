N = int(input())
sum = 0
for i in range(N + 1):
  if i == 0:
    continue
  sum += 10000 * i * 1 / N
print(sum)

# 別解(1とNの真ん中の値をとる)
n = int(input())
print(10000 * (1 + n) / 2)
