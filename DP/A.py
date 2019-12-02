# min関数あったわ!
# def chmin(a, b):
#   if a <= b:
#     return a
#   else:
#     return b 

# 一応abs関数くらいは作るか
def getAbs(a, b):
  return abs(a - b)

# input
N = 6
h = [30, 10, 60, 10, 60, 50]
# N = int(input())
# h = list(map(int, input().split()))

# n個目のhまで渡るのに最小の労力をdp[n]とする
dp = [float("inf")] * N

# 初期値の設定
dp[0] = 0 # 0の初期値は0
dp[1] = getAbs(h[0], h[1]) # 1の初期値はh[0]とh[1]の差

for i in range(2, N):
  dp[i] = min(dp[i], dp[i - 1] + getAbs(h[i], h[i - 1]))
  dp[i] = min(dp[i], dp[i - 2] + getAbs(h[i], h[i - 2]))
  
print(dp[N - 1])