arr = ['A', 'B', 'C', 'D']

for _ in range(3):
    a = list(map(int, input().split()))
    zCount = a.count(0)
    if zCount > 0:
        print(arr[zCount-1])
    else:
        print('E')
