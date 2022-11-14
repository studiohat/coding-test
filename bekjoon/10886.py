rst = 0
rst2 = 0

for _ in range(int(input())):
    tmp = int(input())

    if tmp == 0:
        rst += 1
    else:
        rst2 += 1

if rst2 > rst:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")
    

