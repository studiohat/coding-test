K, N, M = map(int, input().split())

s = (K*N) - M

if s > 0:
    print(s)
else:
    print(0)