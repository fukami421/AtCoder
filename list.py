# listから特定の文字列を全て削除
re = ""
while re in A:
  A.remove(re)

# list内の登場回数
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

# listと文字列の変換
S = list(S)
S = "".join(S)

# list交換
S[l - 1], S[r -1] = S[r - 1], S[l - 1]

# 左からl番目とr番目までをひっくり返す
S[l - 1 : r] = S[l - 1 : r][::-1]
