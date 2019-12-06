W = input()
v = ['a', 'i', 'u', 'e', 'o']
ans = ''
 
for i in W:
    if i not in v:
        ans += i
 
print(ans)

W=input()
for i in W:
        if i in ['a','i','u','e','o']:
                W=W.replace(i, '')
print(W)