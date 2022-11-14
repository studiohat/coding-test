for _ in range(int(input())):
    a = list(input())
    rst = 0
    s = []

    while a:
        if a[0] == "X":
            a.pop(0)
            s = []
        else:
            s.append(a.pop(0))
            rst += len(s)
    
    print(rst)