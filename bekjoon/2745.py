import math

N, B = map(str, input().split())

N = list(N[::-1])

alph = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
result = 0

for i in range(1, len(N)):
    if N[i] in alph:
        result += (alph.index(N[i])+10) * math.pow(int(B), i)
    else:
        result += int(N[i]) * math.pow(int(B), i)

if N[0] in alph:
    result += alph.index(N[0])+10
else:
    result += int(N[0])

print(int(result))
