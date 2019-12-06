s=list(input())
n=int(input())
ans=[]
for i in range(5):
    for j in range(5):
        ans.append(s[i]+s[j])
ans.sort()
print(ans[n-1])

# 別解
s = input()
n = int(input())
print(s[(n-1)//5] + s[(n-1)%5])
