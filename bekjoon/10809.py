alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
         'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

arr = list(input())

result = []

for i in alpha:
    if i in arr:
        result.append(arr.index(i))
    else:
        result.append(-1)

print(" ".join(list(map(str, result))))
