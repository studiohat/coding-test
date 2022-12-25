from itertools import combinations_with_replacement

N = int(input())

arr = [i for i in range(N+1)]

arr = list(combinations_with_replacement(arr,2))

rst = 0

for i in arr:
    rst += sum(i)

print(rst)