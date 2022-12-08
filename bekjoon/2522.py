N = int(input())

for i in range(1, N+1):
    s = N - i
    for _ in range(s):
        print(" ", end="")
    for _ in range(i):
        print("*", end="")
    print()
for i in range(N-1, 0, -1):
    s = N - i
    for _ in range(s):
        print(" ", end="")
    for _ in range(i):
        print("*", end="")
    print()