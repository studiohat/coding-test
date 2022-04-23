n = int(input())

maxN = (n * 2) - 1

for i in range(1, n+1):
    ptN = (i * 2) - 1
    t = int((maxN - ptN) / 2)
    for _ in range(t):
        print(' ', end='')
    for _ in range(ptN):
        print('*', end='')
    print()
