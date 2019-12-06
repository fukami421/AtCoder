n,k,x,y=(int(input()) for i in range(4))
if n - k > 0:
  ans = k * x + (n - k) * y
else:
  ans = n * x
print(ans)
