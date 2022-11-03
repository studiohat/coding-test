import math

for _ in range(int(input())):
    s, n = map(int, input().split())

    print(math.lcm(s, n))