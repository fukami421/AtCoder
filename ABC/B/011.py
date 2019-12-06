S = input()
S = list(S)

for i in range(len(S)):
  if i == 0:
    S[0] = S[0].upper()
  else:
    S[i] = S[i].lower()
S = "".join(S)
print(S)