from collections import deque

a = input()

c = deque()

for i in a:
    if i.isalpha():
        c.append(i.lower())

while len(c) > 1:
    if c.popleft() != c.pop():
        print(False)
        break
else:
    print(True)