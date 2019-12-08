N = int(input())
S = [''] * N
P = [0] * N

for i in range(N):
  s, p = input().split()
  S[i], P[i] = s, int(p)

limit = sum(P) / 2
ans = 'atcoder'

for i in range(N):
  if P[i] > limit:
    ans = S[i]

print(ans)

# 別解(1部)
if max(P)>sum(P)/2:
    print(S[P.index(max(P))])
else:print("atcoder")
