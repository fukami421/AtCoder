# n, m = [6, 0]
n, m = map(int, input().split())
n = n % 12

N = 360 / 12 * n + 360 / 12 * m / 60
M = 360 / 60 * m
angle = abs(N - M)
print(min(360 - angle, angle))
