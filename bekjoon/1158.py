from collections import deque

n, k = map(int, input().split())

deq = deque([i for i in range(1, n + 1)])
arr = []

while deq:
    deq.rotate(-k)
    arr.append(str(deq.pop()))

print('<' + ", ".join(arr) + ">")
