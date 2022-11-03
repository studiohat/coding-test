x, y, z = map(int, input().split())

if x == y and y == z:
    print(10000 + (x *1000))
elif x == y or y == z or x == z:
    if x == y:
        print(1000 + (x*100))
    elif y == z:
        print(1000 + (y*100))
    elif x == z:
        print(1000 + (z*100))
else:
    a = [x,y,z]
    a.sort(reverse= True)
    print(a[0] * 100)