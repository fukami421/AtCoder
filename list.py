# listから特定の文字列を全て削除
re = ""
while re in A:
  A.remove(re)

# list内の1番登場回数が多い要素を取得
# まずSにある各要素を１個だけWに格納
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

# listのsort
org_list.sort(reverse=True)
new_list_reverse = sorted(org_list, reverse=True)

# enumerate
for i, w in enumerate (W):
  if i != len(W) - 1:

# 2次元配列
old_list = [[0 for _ in range(n)] for _ in range(n)]
