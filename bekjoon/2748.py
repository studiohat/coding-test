n = int(input())

i = 0
rst = 0
tmp = 1

while i < n:
    a = rst
    rst += tmp
    tmp = a
    i += 1


print(rst)