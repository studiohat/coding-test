for _ in range(int(input())):
    c, v = map(int, input().split())

    s = c // v
    i = c % v

    print("You get", s, "piece(s) and your dad gets", i, "piece(s).")