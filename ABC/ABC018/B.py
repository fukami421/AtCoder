S = list(input())
N = int(input())

for i in range(N):
  l, r = map(int, input().split())
  S[l - 1 : r] = S[l - 1 : r][::-1]

S = "".join(S)
print(S)