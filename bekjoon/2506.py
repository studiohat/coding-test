N = int(input())

arr = list(map(int, input().split()))

rst = 0 

a = 0

for i in arr:
    if i == 1:
        a += 1
        rst += a
    else:
        a = 0

print(rst)