n = int(input())

for i in range(1, n+1):
    print(' '*((((n*2-1)-(i*2-1)))//2) + '*'*(i*2-1))

for i in range(n-1, 0, -1):
    print(' '*(((n*2-1)-(i*2-1))//2) + '*'*(i*2-1))
