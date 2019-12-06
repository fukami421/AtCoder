N, S, T = map(int, input().split())
W = int(input())
ans = 1 if W >= S and W <= T else 0
for _ in range(N - 1):
  W += int(input())
  if W >= S and W <= T:
    ans += 1
print(ans)
