rst = []

s = int(input())

for _ in range(s):
    a = []
    N, d, m, y = input().split()

    a.append(N)
    a.append(int(d))
    a.append(int(m))
    a.append(int(y))

    rst.append(a)

rst.sort(key=lambda x : (x[3],x[2],x[1]))

print(rst[s-1][0])
print(rst[0][0])

