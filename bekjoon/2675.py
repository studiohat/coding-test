for _ in range(int(input())):
    R, S = input().split()
    S = list(S)

    rst = ''

    for i in range(len(S)):
        rst += (S[i]*int(R))

    print(rst)

