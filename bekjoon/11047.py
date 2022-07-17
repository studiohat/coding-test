N, K = map(int, input().split())
arr = []
result = 0


for _ in range(N):
    arr.append(int(input()))

arr.reverse()

for i in range(N):
    if arr[i] > K:
        continue
    else:
        result += K // arr[i]
        K = K % arr[i]

print(result)
