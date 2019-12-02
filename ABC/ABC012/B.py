def lower10(n):
  if n < 10:
    return "0" + str(n)
  else:
    return str(n)

N = int(input())

h = N // 3600
m = (N - (h * 3600)) // 60
s = N - (h * 3600) - (m * 60)

ans = lower10(h) + ":" + lower10(m) + ":" + lower10(s)
print(ans)
