M = int(input())
N = int(input())

rst = []

for i in range(M, N+1):
    if int(i**0.5)**2 == i:
        rst.append(i)

if len(rst) != 0:
    rst.sort()
    print(sum(rst))
    print(rst[0])
else:
    print(-1)