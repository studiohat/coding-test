xl = {}
yl = {}

for _ in range(3):
    x, y = map(int, input().split())

    if xl.get(x):
        xl[x] += 1
    else:
        xl[x] = 1 

    if yl.get(y):
        yl[y] += 1
    else:
        yl[y] = 1 

xl = list(xl.items())
yl = list(yl.items())

xr = 0
yr = 0

for i in range(2):
    if xl[i][1] == 1:
        xr = xl[i][0]

    if yl[i][1] == 1:
        yr = yl[i][0]

print(str(xr) + " " + str(yr)) 
