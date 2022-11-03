rst = 0

for _ in range(int(input())):
    tmp = 0
    x, y, z = map(int, input().split())

    if x == y and y == z:
        tmp = 10000 + (x *1000)
    elif x == y or y == z or x == z:
        if x == y:
            tmp = 1000 + (x*100)
        elif y == z:
            tmp = 1000 + (y*100)
        elif x == z:
            tmp = 1000 + (z*100)
    else:
        a = [x,y,z]
        a.sort(reverse= True)
        tmp = a[0] * 100
    
    if tmp > rst:
        rst = tmp

print(rst)
