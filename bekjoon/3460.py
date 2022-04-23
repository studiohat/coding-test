for _ in range(int(input())):
    n = list(bin(int(input()))[2::])
    n.reverse()
    for i in range(len(n)):
        if n[i] == '1':
            print(i, end=' ')
