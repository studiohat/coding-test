for _ in range(int(input())):
    rst = {}

    for _ in range(int(input())):
        C, N = input().split()

        rst[N] = int(C)
    
    rst = list(rst.items())

    rst.sort(key=lambda x: (-x[1]))

    print(rst[0][0])