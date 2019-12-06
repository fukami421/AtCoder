s = list(input())
N = len(s)

isFirst = False
first = s[0]
ans = []
count = 1

for i in range(1, N):
  if s[i] == first:
    count += 1
  else:
    ans.append(first)
    ans.append(str(count))
    first = s[i]            
    count = 1

# 最後の文字をappendする
ans.append(first)
ans.append(str(count))

print("".join(ans))
