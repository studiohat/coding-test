for _ in range(int(input())):
    totC = 0
    total = 0
    for _ in range(int(input())):
        C, G = map(float,input().split())
        total += C * G

        totC += C
    
    GPA = total / totC
    print(int(totC), format(GPA, ".1f"))
