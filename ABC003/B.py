S,T=(input() for i in range(2))
v = ['a', 't', 'c', 'o', 'd', 'e', 'r']
s = "You can win"
for i in range(len(S)):
  if S[i] == T[i]:
    continue
  else:
    if S[i] == "@":
      if T[i] in v:
        continue
      else:
        s = "You will lose"
        break
    elif T[i] == "@":
      if S[i] in v:
        continue
      else:
        s = "You will lose"
        break
    else:
      s = "You will lose"
      break
print(s)

# 別解
s,t=(input() for i in range(2))
l = ["a","t","c","o","d","e","r","@"]
for i in range(len(s)):
  if s[i] == "@" and t[i] not in l:
    print("You will lose")
    exit()
  elif t[i] == "@" and s[i] not in l:
    print("You will lose")
    exit()
  elif s[i] != "@" and t[i] != "@" and s[i] != t[i]:
    print("You will lose")
    exit()
  else:
     continue
print("You can win")