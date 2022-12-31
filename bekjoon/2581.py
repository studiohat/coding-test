def find(i):
    if i == 1:
        return False
    else:
        for x in range(2, i):
            if i % x == 0:
                return False
        
        return True

M = int(input())
N = int(input())
rst = []

for i in range(M, N+1):
    if find(i) == True:
        rst.append(i)
    else:
        continue

if len(rst) == 0:
    print(-1)
else:
    print(sum(rst))
    print(min(rst))