# 私の解  
List=[int(i) for i in input().split()]
if List.count(5) == 2 and List.count(7) == 1:
  print("YES")
else:
  print("NO")

# 別解  
abc = input().replace(' ', '')
 
print('YES' if abc.count('7')==1 and abc.count('5')==2 else 'NO')
