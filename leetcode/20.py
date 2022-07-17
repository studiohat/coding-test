a = ['(',')','[',']','{','}']

stack = []

table = {
    "}" : "{",
    "]" : "[",
    ")" : "("
}

for char in a:
    if char not in table:
        stack.append(char)
    elif not stack or table[char] != stack.pop():
        print(False)
        break

