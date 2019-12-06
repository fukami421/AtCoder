_ = int(input())
A = list(map(int, input().split()))

while 0 in A:
  A.remove(0)

sum = sum(A)
ave = sum / len(A)

if ave % 1 == 0:
  print(sum // len(A))
else:
  print(sum // len(A) + 1)
