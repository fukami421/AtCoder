A = input()
n = len(A)

if n > 1:
  print(A[:-1])
else:
  if A == 'a':
    print(-1)
  else:
    print('a')