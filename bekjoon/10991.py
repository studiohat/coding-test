N = int(input())

if N == 1: 
    print("*")
else:
    for i in range(1, N+1):
        print(" "*(N-i),end="")
        for x in range(i):
            print("*",end=" ")
        print()
