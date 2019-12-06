import math

def circle(r):
  return math.pi * r * r

N = int(input())
R = list(int(input()) for _ in range(N))
R.sort(reverse = True)
ans = 0
for i in range(N):
  if i % 2 == 0 and i == N - 1:
    ans += circle(R[i])
  elif i % 2 == 0:
    ans += (circle(R[i]) - circle(R[i + 1]))
print(ans)