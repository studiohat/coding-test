import sys
import heapq

input = sys.stdin.readline

N = int(input())
arr = []
answer = []

for _ in range(N):
    d, c = map(int, input().split())
    arr.append([d,c])

arr.sort()

for i in arr:
    heapq.heappush(answer, i[1])
    if i[0] < len(answer):
        heapq.heappop(answer)

print(sum(answer))

# 3
# 3 9
# 3 4
# 1 1

# 오답:10 정답: 14
# 데드라인 남았는데 넘겨버린 경우

# 3
# 1 25
# 2 50
# 2 100

# 오답: 125 정답: 150
# 데드라인 긴 경우가 더 많은 라면 얻을 수 있는 경우

#출처 : https://www.acmicpc.net/board/view/97635

#풀이 출처 : https://velog.io/@ju_h2/Python-백준-1781.-컵라면-풀이-파이썬-탐욕-알고리즘그리디-구현-6