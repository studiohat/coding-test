s = 0.0

a = list(input())

if len(a) == 2: 

    if a[0] == 'A':
        s = 4.0
    elif a[0] == 'B':
        s = 3.0
    elif a[0] == 'C':
        s = 2.0
    elif a[0] == 'D':
        s = 1.0

    if a[1] == '+':
        s += 0.3
    elif a[1] == '-':
        s -= 0.3

    print(s)
else:
    print(s)