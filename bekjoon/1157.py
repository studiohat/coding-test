from collections import Counter

arr = list(input())
arr = [i.upper() for i in arr]

val = Counter(arr).most_common()

if len(arr) == 1:
    print(val[0][0])
else:
    if val[0][1] == val[1][1]:
        print('?')
    else:
        print(val[0][0])
