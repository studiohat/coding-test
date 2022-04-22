from collections import deque
import sys

deq = deque()

for _ in range(int(sys.stdin.readline())):
    n = sys.stdin.readline().split()

    if n[0] == 'push':
        deq.appendleft(n[1])
    elif n[0] == 'pop':
        if deq:
            print(deq.popleft())
        else:
            print(-1)
    elif n[0] == 'size':
        print(len(deq))
    elif n[0] == 'empty':
        if deq:
            print(0)
        else:
            print(1)
    elif n[0] == 'top':
        if deq:
            print(deq[0])
        else:
            print(-1)
