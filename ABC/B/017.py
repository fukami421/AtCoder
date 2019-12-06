# なぜ間違っているか不明
S = input()

L = len(S)
ans = "NO"
W = ["o", "k", "u"]

if S[:5] == "choku":
  if L == 5:
    ans = "YES"
  elif L == 6:
    if S[-1] in W:
      ans = "YES"
  elif L > 6:
    if S[-1] in W or S[-2:] == "ch":
      ans = "YES"    
print(ans)



# 正解
x = input()
 
a = x.replace("ch", "").replace("o", "").replace("k", "").replace("u", "")
 
if a == "":
    print("YES")
else:
    print("NO")