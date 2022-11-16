for _ in range(int(input())):
    rst = {}
    for _ in range(int(input())):
        s, n = input().split()
        rst[s] = int(n)
    
    rst = list(rst.items())
    rst.sort(key=lambda x: (-x[1]))

    print(rst[0][0])