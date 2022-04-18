for _ in range(int(input())):
    a, b = map(str, input().split())
    result = int(a, 2) + int(b, 2)
    print(bin(result)[2:])
