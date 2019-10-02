'''
https://atcoder.jp/contests/abc042/tasks/abc042_a
'''

List=[int(i) for i in input().split()]
if List.count(5) == 2 and List.count(7) == 1:
  print("YES")
else:
  print("NO")
