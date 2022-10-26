a = int(input())

d = 2 

while d <= a:
    if a % d == 0:
        print(d)
        a = a / d
    else:
        d += 1