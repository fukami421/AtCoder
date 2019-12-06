a, b, n = [int(input()) for _ in range(3)]

#最大公約数
def gcd(a,b):
  while b!=0:
      a, b = b, a % b
  return a

#最小公倍数
def lcm(a,b):
  return a * b // gcd(a,b)

ans = lcm(a,b)
while ans < n:
  ans += lcm(a,b)
print(ans)