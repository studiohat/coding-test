import sys

input = sys.stdin.readline

R, C = map(int, input().split())

visited = [[-1 for _ in range(C)] for _ in range(R)]

arr = [list(input()) for _ in range(R)]

rst = 0

def dfs(x, y):
    if y == C-1:
        return True
    
    for dx in [-1, 0, 1]:
        nx = x + dx
        ny = y + 1

        if 0 <= nx < R and 0 <= ny <=C:
            if arr[nx][ny] != "x" and visited[nx][ny] == -1:
                visited[nx][ny] = 1
                if dfs(nx, ny):
                    return True
        
    return False

for i in range(R):
    if dfs(i, 0):
        rst += 1

print(rst)

#출처 : https://recordofwonseok.tistory.com/370