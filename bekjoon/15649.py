from itertools import permutations

n, m = map(int, input().split())

arr = [i for i in range(1, n+1)]

result = list(map(list, permutations(arr, m)))

for i in result:
    print(*i)
