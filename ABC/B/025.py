def direction(s):
  if s == "East":
    return 1
  else:
    return -1

def count(d, A, B):
  if d < A:
    return A
  elif A <= d <= B:
    return d
  elif d > B:
    return B

def main():
  N, A, B = map(int, input().split())
  goal = 0
  for i in range(N):
    s, _d = map(str, input().split())
    d = int(_d)
    goal += direction(s) * count(d, A, B)
    
  if goal > 0:
    print("East " + str(goal))
  elif goal < 0:
    print("West " + str(abs(goal)))
  else:
    print(0)

main()
