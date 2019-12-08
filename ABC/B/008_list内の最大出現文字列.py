N = int(input())
S = list(input() for _ in range(N))

W = []
for s in S:
  if s not in W:
    W.append(s)

ans = W[0]
for w in W:
  if w == ans:
    continue
  if S.count(ans) < S.count(w):
    ans = w
print(ans)
