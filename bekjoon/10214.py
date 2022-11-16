for _ in range(int(input())):
    rstY = 0
    rstK = 0

    for _ in range(9):
        Y, K = map(int, input().split())

        rstK += K
        rstY += Y

    if rstY == rstK:
        print("Draw")
    elif rstK > rstY:
        print("Korea")
    else:
        print("Yonsei")    