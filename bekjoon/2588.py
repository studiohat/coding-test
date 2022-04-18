a = int(input())
b = input()

result = a * int(b)

b = list(b)
b.reverse()

for i in b:
    mResult = int(i)*a
    print(mResult)

print(result)
