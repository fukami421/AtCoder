N = int(input())
a = list(map(int, input().split()))
# N = 3
# a = [1, 2, 3]

q = sum(a) // len(a)
mod = sum (a) % len(a)

ans = 0
left = a[0]
if mod == 0:
  for i in range(N - 1):
    if left != q * (i + 1):
      ans += 1
    left += a[i + 1]
else:
  ans = -1
print(ans)
