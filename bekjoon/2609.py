A, B = map(int, input().split())

x = 0

y = 0

for i in range(min(A,B), 0, -1):
    if A % i == 0 and B % i == 0:
        x = i
        break

print(x)

y = (A*B) // x

print(y)