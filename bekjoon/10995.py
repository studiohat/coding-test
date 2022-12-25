N = int(input())

if N == 1:
    print("*")
else:
    for i in range(1, N+1):
        if i % 2 != 0:
            for _ in range(N):
                print("*", end=" ")
            print()
        else:
            print(" ",end="")
            for _ in range(N):
                print("*",end=" ")
            print()