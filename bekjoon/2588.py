a = int(input())
b = list(input())

print(a * int(b[2]))
print(a * int(b[1]))
print(a * int(b[0]))

b = ''.join(b)
b = int(b)

print(a*b)