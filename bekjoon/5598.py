str = list(input())

result = []

transStr = {'A': 'X', 'B': 'Y', 'C': 'Z'}

for i in str:
    if i == 'A' or i == 'B' or i == 'C':
        result.append(transStr.get(i))
    else:
        result.append(chr(ord(i)-3))

print(''.join(result))
