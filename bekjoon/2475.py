arr = list(map(int, input().split()))

rst = 0

for i in arr:
    rst += i*i

print(rst%10)