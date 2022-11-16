rstc = 100
rsts = 100

for _ in range(int(input())):
    c, s = map(int,input().split())

    if c == s:
        continue
    elif c > s:
        rsts -= c
    elif s > c:
        rstc -= s

print(rstc)
print(rsts)