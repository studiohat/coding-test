rst = {"Q1" : 0, "Q2" : 0, "Q3" : 0, "Q4" : 0, "AXIS" : 0}

for _ in range(int(input())):
    x, y = map(int, input().split())
    
    if x == 0 or y == 0:
        rst["AXIS"] += 1
    elif x > 0 and y > 0:
        rst["Q1"] += 1
    elif x <0 and y > 0:
        rst["Q2"] += 1
    elif x < 0 and y < 0:
        rst["Q3"] += 1
    elif x > 0 and y <0:
        rst["Q4"] += 1

print("Q1: " + str(rst["Q1"]))
print("Q2: " + str(rst["Q2"]))
print("Q3: " + str(rst["Q3"]))
print("Q4: " + str(rst["Q4"]))
print("AXIS: " + str(rst["AXIS"]))
