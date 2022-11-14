while True:
    n = int(input())
    a = []

    if n == -1:
        break
    
    for i in range(1, n):
        if n % i == 0:
            a.append(i)


    if n == sum(a):
        a = map(str, a)
        s = ' + '.join(a)
        print(n,"=",s )
    else:
        print(n,"is NOT perfect.")

