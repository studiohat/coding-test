from collections import deque
import sys

deq = deque()

for _ in range(int(sys.stdin.readline())):
    n = sys.stdin.readline().split()

    if n[0] == 'push_front':
        deq.appendleft(n[1])
    elif n[0] == 'push_back':
        deq.append(n[1])
    elif n[0] == 'pop_front':
        if deq:
            print(deq.popleft())
        else:
            print(-1)

    elif n[0] == 'pop_back':
        if deq:
            print(deq.pop())
        else:
            print(-1)

    elif n[0] == 'size':
        print(len(deq))
    elif n[0] == 'empty':
        if deq:
            print(0)
        else:
            print(1)
    elif n[0] == 'front':
        if deq:
            print(deq[0])
        else:
            print(-1)
    elif n[0] == 'back':
        if deq:
            print(deq[len(deq)-1])
        else:
            print(-1)
