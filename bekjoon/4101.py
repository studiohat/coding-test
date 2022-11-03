while 1:
    n1, n2 = map(int, input().split())

    if n1 > n2:
        print("Yes")
    elif n1 == 0 and n2 ==0:
        break
    else:
        print("No")