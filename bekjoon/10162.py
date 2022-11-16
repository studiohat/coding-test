T = int(input())

A = 300
B = 60
C = 10

rstA = 0
rstB = 0
rstC = 0

if T % 10 != 0:
    print(-1)
else:
    while T > 0:
        if T >= 300:
            rstA += T // A
            T = T % A
        elif T >= 60:
            rstB += T // B
            T = T % B
        else:
            rstC += T // C
            T = T % C
    
    print(rstA,rstB,rstC)

