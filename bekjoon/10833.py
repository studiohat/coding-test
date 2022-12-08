rst = 0

for _ in range(int(input())):
    S, A = map(int, input().split())

    rst += A % S

print(rst)