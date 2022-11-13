for _ in range(int(input())):
    r, e, c = map(int, input().split())

    e -= c

    if r > e:
        print("do not advertise")
    elif r == e:
        print("does not matter")
    else:
        print("advertise")