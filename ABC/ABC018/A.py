p = [int(input()) for _ in range(3)]
 
p_sort = sorted(p, reverse=True)
for item in p:
  print(p_sort.index(item)+1)