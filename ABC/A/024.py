A, B, C, K = map(int, input().split())
S, T = map(int, input().split())
N = S + T
ans = A * S + B * T
print(ans if N < K else ans - C * N)