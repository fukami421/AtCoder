N = int(input())
twos = [8, 4, 2, 1]
ans = []
while N != 0:
  for i in twos:
    if i <= N:
      N -= i
      ans.append(i)
      if N == 0:
        print(len(ans))
        for j in ans:
          print(j)

# 別解
N = int(input())
print(N)
for i in range(N):
    print(1)