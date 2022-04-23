from collections import deque

a = []

for _ in range(int(input())):
    n = input().split()
    for i in n:
        s = deque(list(i))
        s.reverse()
        print("".join(list(s)), end=" ")
    print()
