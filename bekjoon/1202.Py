import sys
import heapq

input = sys.stdin.readline

N, K = map(int, input().split())

J = []
B = []

rst = 0

for _ in range(N):
    heapq.heappush(J,list(map(int, input().split())))

for _ in range(K):
    B.append(int(input()))

B.sort()

tmpJ = []

for i in B:
    while J and i >= J[0][0]:
        heapq.heappush(tmpJ, -heapq.heappop(J)[1])
    if tmpJ:
        rst -= heapq.heappop(tmpJ)
    elif not J:
        break



print(rst)


# 가장 작은 가방에 가장 비싼 보석 값 넣기 
# 가장 작은 가방 안에 들어갈 보석을 찾으면서 최대 힙을 이용하여 해당 크기보다 작은 경우 모두 담고 거기서 가장 큰 값을 결과에 더함 
# 이때 보석이 존재 하지 않으면 종료 

#출처 : https://velog.io/@piopiop/백준-1202-보석-도둑-Python