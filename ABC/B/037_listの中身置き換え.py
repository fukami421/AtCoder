N, Q = map(int, input().split())
W = [0] * N
L = [0] * Q
R = [0] * Q
T = [0] * Q
for i in range(Q):
  L[i], R[i], T[i] = map(int, input().split())

for i in range(Q):
  for j in range(L[i], R[i] + 1): # 最後の数に注意
    W[j - 1] = T[i]

for i in range(N):
  print(W[i])

# 別解
N, Q = [4, 5]
a = [0] * N
 
for _ in range(Q):
    L, R, T = [3, 4, 7]
    a[L - 1:R] = [T] * (R - L + 1) # 長さは左右等しく！
 
for i in a:
    print(i)