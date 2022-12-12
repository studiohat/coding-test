import sys

N = int(sys.stdin.readline())
rst = 0

for _ in range(N):
    rst += int(sys.stdin.readline())

print(rst-(N-1))