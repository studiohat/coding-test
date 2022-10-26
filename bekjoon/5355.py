for _ in range(int(input())):
    a = list(input().split())

    a.reverse()

    num = float(a.pop())

    while a:
        x = a.pop()

        if x == '@':
            num *= 3
        elif x == '%':
            num += 5
        else:
            num -= 7
    
    num = '{:.2f}'.format(num)

    print(num)