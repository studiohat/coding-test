from collections import deque
import sys

arr = deque()

for _ in range(int(sys.stdin.readline())):
    n = sys.stdin.readline()
    n = n.split()
    if n[0] == 'push':
        arr.append(n[1])
    elif n[0] == 'pop':
        if len(arr) != 0:
            print(arr.popleft())
        else:
            print(-1)
    elif n[0] == 'size':
        print(len(arr))
    elif n[0] == 'empty':
        if len(arr) != 0:
            print(0)
        else:
            print(1)
    elif n[0] == 'front':
        if len(arr) != 0:
            print(arr[0])
        else:
            print(-1)
    elif n[0] == 'back':
        if len(arr) != 0:
            print(arr[len(arr)-1])
        else:
            print(-1)
