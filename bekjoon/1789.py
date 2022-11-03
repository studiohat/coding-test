n = int(input())

sum = 0


for i in range(1, 4294967295):
    sum += i

    if sum > n:
        print(i-1)
        break
