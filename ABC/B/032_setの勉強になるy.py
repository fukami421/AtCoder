# https://atcoder.jp/contests/abc032/tasks/abc032_b
s = input()
k = int(input())
if len(s) < k:
    ans = 0
elif len(s) == k:
    ans = 1
else:
    S = set()
    for i in range(len(s)-k+1):
        a = s[i:i+k]
        S.add(a)
    ans = len(S)
print(ans)