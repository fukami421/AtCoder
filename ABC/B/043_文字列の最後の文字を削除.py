S = list(input())

ans = ''
for s in S:
  if s == '0':
    ans += s
  elif s == '1':
    ans += s
  else:
    ans = ans[:-1]
print(ans)
