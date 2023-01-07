n = int(input())

n1 = 0
n2 = 1

rst = 0

if n == 1:
    print(1)
else:
    for _ in range(2, n+1):
        rst = n1 + n2
        n1 = n2
        n2 = rst
    print(rst)
