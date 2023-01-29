import sys

input = sys.stdin.readline

N, C = map(int, input().split())

M = int(input())

arr = []

for _ in range(M):
    stv, env, bn = map(int, input().split())
    arr.append([stv, env, bn])

arr.sort(key= lambda x: (x[1]))

capa = [C]*N
total = 0

for s, r, box in arr:
    _min = C
    for i in range(s, r):
        if _min > min(capa[i], box):
            _min = min(capa[i], box)
    for i in range(s, r):
        capa[i] -= _min
    total += _min
print(total)

#풀이 출처 : https://ddiyeon.tistory.com/36