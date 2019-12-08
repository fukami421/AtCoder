A, B, C = input().split()

turn = 'a'

while l != 0:
  if turn == 'a':
    turn = A[0]
    A = A[1:]
  elif turn == 'b':
    turn = B[0]
    B = B[1:]
  else:
    turn = C[0]
    C = C[1:]

  if turn == 'a':
    l = len(A)
  elif turn == 'b':
    l = len(B)
  else:
    l = len(B)
print(turn)

