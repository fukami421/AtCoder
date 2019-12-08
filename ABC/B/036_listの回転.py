N = int(input())
S = list(input() for _ in range(N))

W = [''] * N
for i in range(N):
  w = ''
  for j in range(N):
    w += S[N - 1 - j][i]
  W[i] = w
for i in range(N):
  print("".join(W[i]))
