L, H = map(int, input().split())
N = int(input())

for _ in range(N):
  a = int(input())
  if a < L:
    print(L - a)
  elif a <= H:
    print(0)
  else:
    print(-1)


# 別解(1部)
  a = int(input())
  if a > h:
    print(-1)
  else:
    print(max(l - a, 0))