m = int(input()) / 1000
ans = ""
if m < 0.1:
  print("00")
  # ans = 
elif m <= 5:
  if m < 1:
    print("0" + str(int(m * 10)))
  else:
    print(str(int(m * 10)))
elif m <= 30:
  print(str(int(m + 50)))
elif m <= 70:
  print(str(int((m - 30) // 5 + 80)))
else:
  print("89")
