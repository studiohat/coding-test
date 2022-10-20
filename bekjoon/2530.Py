t, m, s = map(int,(input().split()))
c = int(input())

s = s+c

while s >= 60:
    s -= 60
    m += 1

while m >= 60:
    m -= 60
    t += 1

while t >= 24:
    t -= 24

print(str(t) + ' ' + str(m) + ' ' + str(s))