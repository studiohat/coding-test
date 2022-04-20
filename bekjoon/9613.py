from itertools import combinations


def GCD(a, b):
    while(b):
        a, b = b, a % b
    return a


def LCM(a, b):
    result = (a*b) // GCD(a, b)
    return result


result = 0

for _ in range(int(input())):
    N, *arr = map(int, input().split())
    arrG = list(map(list, combinations(arr, 2)))
    for i in arrG:
        result += GCD(i[0], i[1])
    print(result)
    result = 0
