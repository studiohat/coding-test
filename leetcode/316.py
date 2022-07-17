def a(arr):
    tmp = list(set(list(arr)))
    print(tmp)
    tmp.sort()
    

    return "".join(tmp)


s = "bcabc"

print(a(s))

s1 = "cbacdcbc"
print(a(s1))