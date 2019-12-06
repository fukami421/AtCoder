A = input()
B = input()

if len(A) >= len(B):
  print(A)
else:
  print(B)

# 別解
a = input()
b = input()
print(a if len(a) > len(b) else b)
