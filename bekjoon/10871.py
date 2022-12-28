N, X = map(int, input().split())

A = list(map(int, input().split()))

rst = []

for i in A:
    if i < X:
        rst.append(i)

print(" ".join(map(str,rst)))