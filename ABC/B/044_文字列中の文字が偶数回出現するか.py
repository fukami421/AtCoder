_w = list(input())

W = []

for w in _w:
  if w not in W:
    W.append(w)

for w in W:
  if _w.count(w) % 2 != 0:
    print('No')
    exit()

print('Yes')