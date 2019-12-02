N = int(input())
A = list(int(input()) for _ in range(N))
re = max(A)

while re in A:
  A.remove(re)

print(max(A))