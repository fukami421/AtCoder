# 合ってるけれど、実行時間超過
n = int(input())
a = [0] * n

sum_a = 0

if n >= 3:
  a[2] = 1

if n > 3:
  for i in range(3, n):
    a[i] = a[i - 1] + a[i - 2] + a[i - 3]
ans = a[n - 1] % 10007
print(ans)

