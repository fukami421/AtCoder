N, T = map(int, input().split())
A = list(int(input()) for _ in range(N))

ans = 0
for i in range(N - 1):
  dif = A[i + 1] - A[i]
  if dif < T:
    ans += dif
  else:
    ans += T

print(ans + T)
