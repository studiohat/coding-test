N = int(input())

for i in range(1, N+1):
    for _ in range(i-1):
        print(" ",end="")
    for _ in range(2*N-(2*i-1)):
        print("*",end="")
    print()
for i in range(N-1, 0, -1):
    for _ in range(i-1):
        print(" ",end="")
    for _ in range(2*N-(2*i-1)):
        print("*",end="")
    print()