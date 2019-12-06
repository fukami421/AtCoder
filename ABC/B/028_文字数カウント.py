S = list(input())
W = ["A", "B", "C", "D", "E", "F"]
ans = ""
for i, w in enumerate (W):
  if i != len(W) - 1:
    ans += str(S.count(w)) + " "
  else:
    ans += str(S.count(w))

print(ans)