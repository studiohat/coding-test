def find(i):
    if i == 1:
        return False
    else:
        for x in range(2, i):
            if i % x == 0:
                return False
        
        return True


N = int(input())

arr = map(int, input().split())

rst = 0

for i in arr:
    if find(i) == True:
        rst += 1
    else:
        continue

print(rst)