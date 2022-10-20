t, m = map(int,(input().split()))
c = int(input())

m = m+c

while m >= 60:
    m -= 60
    t += 1

if t >= 24:
    t -= 24

print(str(t) + ' ' + str(m))