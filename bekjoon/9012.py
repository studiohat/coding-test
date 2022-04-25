from collections import deque

for _ in range(int(input())):
    arr = list(input())
    deq = deque()
    flag = True

    for i in arr:
        if i == '(':
            deq.append(i)
        elif len(deq) > 0 and i == ')':
            deq.pop()
        elif len(deq) == 0 and i == ')':
            flag = False
            break
    if not flag:
        print('NO')
    elif len(deq) > 0:
        print('NO')
    else:
        print('YES')
