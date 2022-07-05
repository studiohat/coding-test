from collections import deque

lst = [1,2,2,1]

q = deque(lst)

if not lst:
    print(False)

while len(q) > 1:
    if q.popleft() != q.pop():
        print(False)
        break
else:
    print(True)






