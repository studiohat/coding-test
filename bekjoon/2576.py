arr = [int(input()) for _ in range(7)]

result = []

for i in arr:
    if i % 2 != 0:
        result.append(i)

if result:
    print(sum(result))
    print(min(result))
else:
    print(-1)
