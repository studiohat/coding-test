N, B = map(int, input().split())

arr = []
alph = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


while N >= 1:
    n = N % B
    if n > 9:
        arr.append(alph[n - 10])
        N = N // B
    else:
        arr.append(n)
        N = N // B

arr.reverse()

print("".join(map(str, arr)))
