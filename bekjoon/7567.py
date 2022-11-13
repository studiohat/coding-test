a = list(input())
rst = 0
tmp = ""

for i in range(len(a)):
    if i == 0:
       rst += 10
       tmp = a[i]
    else:
        if tmp == a[i]:
            rst += 5
        else:
            rst += 10
        tmp = a[i]
    

print(rst)