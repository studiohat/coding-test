N = int(input())

arr = list(map(int, input().split()))

arr.sort()

rst = 0

for i in range(1,N+1):
    rst += sum(arr[:i])

print(rst)
