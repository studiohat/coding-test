H, M = map(int, input().split())

s = M - 45

if s < 0:
    if H == 0:
        H = 23
    else:
        H -= 1
    M = 60 + s
else:
    M = M -45

print(str(H) + " " + str(M))