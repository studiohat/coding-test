K = int(input())
arr = [int(input()) for _ in range(K)]

arr.sort(reverse=True)

for i in range(K):
    arr[i] = arr[i] * (i+1)
    

print(max(arr))
        