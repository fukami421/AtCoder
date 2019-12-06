A, B = map(int, input().split())
ans = B / A
print(int(ans))

# 別解(切り捨て除算 ://)
A, B = map(int, input().split())
ans = B // A
print(ans)
